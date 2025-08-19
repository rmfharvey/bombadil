import os
from linear_api import LinearClient, LinearIssue, LinearIssueInput, LinearProject, LinearUser, LinearPriority
from galvanic import colored_logger


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
        self._available_projects = {l.name: l.model_dump() for l in self._target_team.labels}

    def create_issue(
        self, title, description, project, assignee=None, priority=LinearPriority.NONE, labels=[], post=False
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
            label_ids.append(self._available_projects[label]["id"])

        # Create a new issue
        issue_input = LinearIssueInput(
            title=title,
            description=description,
            teamName=self._target_team.name,
            priority=priority,
            assigneeId=assignee.id,
            project=project.name,
            labelIds=label_ids,
        )
        new_issue = self._client.issues.create(issue_input)
        return new_issue


LinearHelper.TARGET_TEAM_NAME = "Electrical"
