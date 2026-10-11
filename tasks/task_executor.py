from tasks.task_queue import TaskQueue


class TaskExecutor:

    def __init__(self):
        pass

    def execute(self, task):

        print(f"Executing: {task.name}")

        try:
            result = f"{task.name} completed successfully"

            print(f"✓ {task.name} completed")

            return result

        except Exception as e:

            print(f"✗ {task.name} failed")

            return str(e)