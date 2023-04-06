from common.task_list import TaskList

b = TaskList("Solve world hunger.", "Create a starting task list outlining required steps to meet objective.")
b.add_todo("buy carrot seeds")
b.add_todo("plant carrot seeds")
b.add_todo("eat carrots")

b.print()

c = b.get_next_task()
b.add_complete(c)

b.print()
