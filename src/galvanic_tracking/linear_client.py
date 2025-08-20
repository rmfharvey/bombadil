import os
import json
from enum import Enum
from pydantic_core._pydantic_core import ValidationError
from linear_api import LinearClient, LinearIssue, LinearIssueInput, LinearProject, LinearUser, LinearPriority
from galvanic import colored_logger

PRIORITY_MAPPING = {p.name: p.value + 1 for p in LinearPriority}
PRIORITY_MAPPING[None] = 0
PRIORITY_MAPPING[LinearPriority.NONE.name] = 0


class LinearTimeEstimate(Enum):
    NONE = 0
    XS = 1
    S = 2
    M = 3
    L = 4
    XL = 5


TIME_ESTIMATE_MAPPING = {e.name: e.value for e in LinearTimeEstimate}
TIME_ESTIMATE_MAPPING[None] = LinearTimeEstimate.NONE.value


class LinearHelper:
    TARGET_TEAM_NAME = None

    def __init__(self, api_key: str = None):
        self.logger = colored_logger(self.__class__.__name__)
        if api_key is None:
            self.logger.info("No Linear API key passed in.  Attempting to load from environment variables")
            api_key = os.environ.get("LINEAR_API_KEY")
            assert (
                api_key is not None
            ), "Linear API key not passed in or found in environment variables.  Pass a key in as 'api_key' or set environment variable 'LINEAR_API_KEY"
        self._client = LinearClient(auto_unwrap_connections=True)

        # Get teams by name
        teams = {t.name: t for t in self._client.teams.get_all().values()}
        self._target_team = teams[self.TARGET_TEAM_NAME]

        self._available_members = {m.name: m.model_dump() for m in self._target_team.members}
        self._available_projects = {p.name: p for id, p in self._target_team.projects.items()}
        self._available_labels = {l.name: l.model_dump() for l in self._target_team.labels}

    def create_issue(
        self,
        title,
        description,
        project,
        assignee=None,
        priority=LinearPriority.NONE,
        labels=[],
        estimate=None,
        post=False,
        parent_issue=None,
    ):
        # Get project
        if isinstance(project, str):
            project = self._available_projects.get(project)

        # Get assignee
        if not isinstance(assignee, LinearUser):
            assignee = project.members[0]

        # Get label IDs
        label_ids = []
        for label in labels:
            label_ids.append(self._available_labels[label]["id"])

        if priority in PRIORITY_MAPPING:
            priority = PRIORITY_MAPPING[priority]

        if estimate in TIME_ESTIMATE_MAPPING:
            estimate = TIME_ESTIMATE_MAPPING[estimate]

        if isinstance(parent_issue, LinearIssue):
            parent_issue = parent_issue.id
        else:
            parent_issue = None

        # Unwrap description
        if isinstance(description, list):
            description = "".join(description)

        # Create a new issue
        try:
            issue_input = LinearIssueInput(
                title=title,
                description=description,
                teamName=self._target_team.name,
                priority=priority,
                assigneeId=assignee.id,
                project=project.name,
                labelIds=label_ids,
                parentId=parent_issue,
                estimate=estimate,
                metadata={
                    "source": "galvanic.LinearHelper",
                    "automated": True
                }
            )
            issue_input.projectName = project.name  # API doesn't set this properly, so do it here
            retval = issue_input
            if post:
                new_issue = self._client.issues.create(issue_input)
                retval = new_issue
            return retval
        except ValidationError as err:
            self.logger.error(err)
            return None

    def create_issues_from_json(self, json_tasks: list, project: str, labels: list = [], element_name: str=None, post: bool=False):
        new_issues = []
        with open(json_tasks, "r") as f:
            task_info = json.load(f)
            tasks = task_info['tasks']

            ### Create parent issue if needed
            create_subissues = task_info['options']["create_subissues"]
            parent_issue = None
            if create_subissues:
                assert element_name is not None, "Element name must be provided if creating subissues"
                kw = {
                    'title': f"{element_name} Validation",
                    "description": f"Validation issues for {element_name}",
                    "project": project,
                }
                time_estimate = task_info['options'].get("parent_time_estimate", LinearTimeEstimate.L.name)
                parent_issue = self.create_issue(estimate=time_estimate, labels=labels, post=post, **kw)

            for task in tasks:
                task['parent_issue'] = parent_issue

                if element_name:    # Prepend title with element name if it exists
                    task['title'] = f"{element_name} - {task['title']}"

                new_issue = self.create_issue(project=project, post=post, **task)

                new_issues.append(new_issue)
        new_issues = list(filter(lambda i: i is not None, new_issues))
        return new_issues


LinearHelper.TARGET_TEAM_NAME = "Electrical"
