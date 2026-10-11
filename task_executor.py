from tasks.task_planner import TaskPlanner
from tasks.task_executor import TaskExecutor

planner = TaskPlanner()
executor = TaskExecutor()

tasks = planner.create_plan("Build Ultron")

executor.load_tasks(tasks)

executor.execute()

print("\nFinal Status")
print(executor.status())