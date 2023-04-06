import unittest
import uuid

from taskmaster.common import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("Test Task", "Test Objective")

    def test_task_has_id(self):
        self.assertIsInstance(uuid.UUID(self.task.id), uuid.UUID)

    def test_task_has_name(self):
        self.assertEqual(self.task.name, "Test Task")

    def test_task_has_objective(self):
        self.assertEqual(self.task.objective, "Test Objective")

    def test_task_has_no_result_initially(self):
        self.assertIsNone(self.task.result)

    def test_task_has_no_completion_order_initially(self):
        self.assertIsNone(self.task.completion_order)

    def test_task_can_be_created_with_given_id(self):
        task = Task("Test Task", "Test Objective", id="123")
        self.assertEqual(task.id, "123")


if __name__ == "__main__":
    unittest.main()
