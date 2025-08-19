from linear_api import LinearPriority
from galvanic_validation.tasks.enums import TASK_TYPE, VALIDATION_PHASE
from galvanic import global_logger


class Task:
    title: str = None
    type: TASK_TYPE = TASK_TYPE.VALIDATION
    description: str = None
    priority: LinearPriority.NONE
    labels: list = []
    AVAILABLE_LABELS: list = []  # Set this before based on project

    def __init__(
        self,
        title: str,
        type: TASK_TYPE,
        description: str,
        priority: LinearPriority = LinearPriority.NONE,
        labels: list = [],
    ):
        try:
            assert type in TASK_TYPE.as_list(), f"Invalid task type: {type}"
            assert priority in LinearPriority, f"Invalid priority: {priority}"
            for label in labels:
                assert label in self.AVAILABLE_LABELS, f"Invalid label: {label}"
        except AssertionError as err:
            global_logger.error(err)
            raise err

        self.title = title
        self.type = type
        self.description = description
        self.priority = priority
        self.labels = labels
