from tasks.task import Task
from tasks.task_queue import TaskQueue

queue = TaskQueue()

queue.add_task(Task("Vision", None, priority=7))
queue.add_task(Task("Speech", None, priority=10))
queue.add_task(Task("Memory", None, priority=5))

print(queue.status())

task = queue.next_task()

print(task)

queue.complete_task(task, "Done")

print(queue.status())