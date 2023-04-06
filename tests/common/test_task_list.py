from unittest import TestCase
from unittest.mock import call, patch

from taskmaster.common import Task, TaskList


class TestTaskList(TestCase):
    def setUp(self):
        self.task_list = TaskList("Test Objective", "Test Task 1")

    def test_init(self):
        self.assertIsNotNone(self.task_list.id)
        self.assertEqual(self.task_list.objective, "Test Objective")
        self.assertEqual(len(self.task_list.todo_tasks), 1)
        self.assertEqual(len(self.task_list.complete_tasks), 0)

    def test_init_with_id(self):
        task_list = TaskList("Test Objective", "Test Task 1", "1234")
        self.assertEqual(task_list.id, "1234")

    def test_add_todo(self):
        self.task_list.add_todo("Test Task 2")
        self.assertEqual(len(self.task_list.todo_tasks), 2)
        self.assertEqual(self.task_list.todo_tasks[1].name, "Test Task 2")

    def test_add_complete(self):
        task = Task("Test Task", "Test Objective")
        self.task_list.add_complete(task)
        self.assertEqual(len(self.task_list.complete_tasks), 1)
        self.assertEqual(self.task_list.complete_tasks[task.id], task)

    def test_get_next_task(self):
        task = self.task_list.get_next_task()
        self.assertEqual(task.name, "Test Task 1")
        self.assertEqual(len(self.task_list.todo_tasks), 0)

    def test_get_todo_list(self):
        self.task_list.add_todo("Test Task 2")
        todo_list = self.task_list.get_todo_list()
        self.assertEqual(len(todo_list), 2)
        self.assertEqual(todo_list[0], "Test Task 1")
        self.assertEqual(todo_list[1], "Test Task 2")

    def test_get_complete_list(self):
        task = Task("Test Task", "Test Objective")
        self.task_list.add_complete(task)
        complete_list = self.task_list.get_complete_list()
        self.assertEqual(len(complete_list), 1)
        self.assertEqual(complete_list[0], "Test Task")

    def test_print_objective(self):
        with patch("builtins.print") as mock_print:
            self.task_list.print_objective()
            mock_print.assert_has_calls(
                [
                    call("\033[94mObjective\033[0m"),
                    call("  Test Objective"),
                ]
            )

    def test_print_todo(self):
        self.task_list.add_todo("Test Task 2")
        with patch("builtins.print") as mock_print:
            self.task_list.print_todo()
            mock_print.assert_has_calls(
                [
                    call("\033[94mTodo Task List\033[0m"),
                    call("  1: Test Task 1"),
                    call("  2: Test Task 2"),
                ]
            )

    def test_print_complete(self):
        task = Task("Test Task", "Test Objective")
        self.task_list.add_complete(task)
        with patch("builtins.print") as mock_print:
            self.task_list.print_complete()
            mock_print.assert_has_calls(
                [
                    call("\033[94mComplete Task List\033[0m"),
                    call("  1: Test Task"),
                ]
            )

    def test_print(self):
        self.task_list.add_todo("Test Task 2")
        task = Task("Test Task", "Test Objective")
        self.task_list.add_complete(task)
        with patch("builtins.print") as mock_print:
            self.task_list.print()
            mock_print.assert_has_calls(
                [
                    call("\033[94mObjective\033[0m"),
                    call("  Test Objective"),
                    call("\033[94mTodo Task List\033[0m"),
                    call("  1: Test Task 1"),
                    call("  2: Test Task 2"),
                    call("\033[94mComplete Task List\033[0m"),
                    call("  1: Test Task"),
                    call("-------------------------------------------------------------------------------------------------------"),
                ]
            )

    def test_to_json(self):
        task_list = TaskList("objective")
        expected = '{"id": "' + str(task_list.id) + '", "objective": "objective", "todo_tasks": [], "complete_tasks": {}}'
        self.assertEqual(task_list.to_json(), expected)

    def test_from_json(self):
        json_string = (
            '{"id": "mock_id", "objective": "objective", "todo_tasks": [{"id": "mock_id", "name": "task1", "objective": "objective", "result": null, "completion_order": null}], "complete_tasks": {}}'
        )
        task_list = TaskList.from_json(json_string)
        self.assertIsInstance(task_list, TaskList)
        self.assertEqual(task_list.id, "mock_id")
        self.assertEqual(task_list.objective, "objective")
        self.assertEqual(len(task_list.todo_tasks), 1)
        self.assertEqual(task_list.todo_tasks[0].name, "task1")
        self.assertEqual(task_list.todo_tasks[0].id, "mock_id")
        self.assertEqual(len(task_list.complete_tasks), 0)

        # Test with complete_tasks
        json_string = '{"id": "mock_id", "objective": "objective", "todo_tasks": [], "complete_tasks": {"mock_id": {"id": "mock_id", "name": "task1", "objective": "objective", "result": "done", "completion_order": 1}}}'
        task_list = TaskList.from_json(json_string)
        self.assertEqual(len(task_list.complete_tasks), 1)
        self.assertEqual(task_list.complete_tasks["mock_id"].name, "task1")
        self.assertEqual(task_list.complete_tasks["mock_id"].result, "done")
        self.assertEqual(task_list.complete_tasks["mock_id"].completion_order, 1)

        # Test with both todo_tasks and complete_tasks
        json_string = '{"id": "mock_id", "objective": "objective", "todo_tasks": [{"id": "mock_id", "name": "task1", "objective": "objective", "result": null, "completion_order": null}], "complete_tasks": {"mock_id": {"id": "mock_id", "name": "task2", "objective": "objective", "result": "done", "completion_order": 1}}}'
        task_list = TaskList.from_json(json_string)
        self.assertEqual(len(task_list.todo_tasks), 1)
        self.assertEqual(task_list.todo_tasks[0].name, "task1")
        self.assertEqual(task_list.todo_tasks[0].id, "mock_id")
        self.assertEqual(len(task_list.complete_tasks), 1)
        self.assertEqual(task_list.complete_tasks["mock_id"].name, "task2")
        self.assertEqual(task_list.complete_tasks["mock_id"].result, "done")
        self.assertEqual(task_list.complete_tasks["mock_id"].completion_order, 1)
