class WorkflowHistory:

    def __init__(self):

        self.history = []

    def add(self, workflow):

        self.history.append(workflow)

    def all(self):

        return self.history

    def clear(self):

        self.history.clear()