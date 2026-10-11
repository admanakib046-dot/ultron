
from tasks.task_planner import TaskPlanner

planner = TaskPlanner()

tasks = planner.create_plan("Build an AI assistant")

for task in tasks:
    print(task)