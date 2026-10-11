import threading


class BackgroundJob(threading.Thread):

    def __init__(self, workflow, executor):

        super().__init__()

        self.workflow = workflow
        self.executor = executor

        self.status = "Pending"

    def run(self):

        self.status = "Running"

        for task in self.workflow:

            self.executor.execute(task)

        self.status = "Completed"