import uuid


class Task:
    """
    A class representing a single task with a unique ID, name, and objective.
    The result and completion order attributes are set when the task is completed.
    """

    def __init__(self, name: str, objective: str, id: str = None) -> None:
        self.id = str(uuid.uuid4()) if id is None else id
        self.name = name
        self.objective = objective
        self.result = None
        self.completion_order = None
