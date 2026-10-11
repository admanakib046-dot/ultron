class Workflow:

    def __init__(self, name):

        self.name = name

        self.tasks = []

    def add(self, task):

        self.tasks.append(task)

    def __iter__(self):

        return iter(self.tasks)

    def __len__(self):

        return len(self.tasks)

    def __str__(self):

        return f"{self.name} ({len(self.tasks)} tasks)"