import json
import uuid
from collections import deque
from typing import List

from .colours import DEFAULT, LIGHT_BLUE
from .task import Task


class TaskList:
    """
    A class representing a list of tasks with a unique ID and objective.
    Tasks are separated into two categories: todo_tasks (incomplete) and complete_tasks (completed).
    """

    def __init__(self, objective: str, first_task: str = None, id: str = None) -> None:
        self.id = str(uuid.uuid4()) if id is None else id
        self.objective = objective
        self.todo_tasks = deque()
        self.complete_tasks = {}
        if first_task is not None:
            self.add_todo(first_task)

    @property
    def todo_count(self) -> int:
        return len(self.todo_tasks)

    @property
    def complete_count(self) -> int:
        return len(self.complete_tasks)

    def add_todo(self, task: str) -> None:
        self.todo_tasks.append(Task(task, self.objective))

    def add_complete(self, task: Task) -> None:
        task.completion_order = self.complete_count + 1
        self.complete_tasks[task.id] = task

    def get_next_task(self) -> Task:
        return self.todo_tasks.popleft()

    def get_todo_list(self) -> List[str]:
        return [task.name for task in self.todo_tasks]

    def get_complete_list(self) -> List[str]:
        return [task.name for task in self.complete_tasks.values()]

    def print_objective(self) -> None:
        print(f"{LIGHT_BLUE}Objective{DEFAULT}")
        print(f"  {self.objective}")

    def print_todo(self) -> None:
        print(f"{LIGHT_BLUE}Todo Task List{DEFAULT}")
        for i in range(self.todo_count):
            print(f"  {i+1}: {self.todo_tasks[i].name}")

    def print_complete(self) -> None:
        print(f"{LIGHT_BLUE}Complete Task List{DEFAULT}")
        for i in self.complete_tasks:
            print(f"  {self.complete_tasks[i].completion_order}: {self.complete_tasks[i].name}")

    def print(self) -> None:
        self.print_objective()
        self.print_todo()
        self.print_complete()
        print("-------------------------------------------------------------------------------------------------------")

    def to_json(self) -> str:
        task_list_data = {
            "id": self.id,
            "objective": self.objective,
            "todo_tasks": [vars(task) for task in self.todo_tasks],
            "complete_tasks": {task_id: vars(task) for task_id, task in self.complete_tasks.items()},
        }
        return json.dumps(task_list_data)

    @classmethod
    def from_json(cls, json_string) -> "TaskList":
        data = json.loads(json_string)
        task_list = cls(objective=data["objective"], id=data["id"])
        for task_data in data["todo_tasks"]:
            task = Task(name=task_data["name"], objective=task_data["objective"], id=task_data["id"])
            task_list.todo_tasks.append(task)
        for task_id, task_data in data["complete_tasks"].items():
            task = Task(name=task_data["name"], objective=task_data["objective"], id=task_data["id"])
            task.result = task_data["result"]
            task.completion_order = task_data["completion_order"]
            task_list.complete_tasks[task_id] = task
        return task_list
