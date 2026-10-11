from datetime import datetime


class Task:

    def __init__(
        self,
        name,
        action,
        data=None,
        priority=5,
        depends_on=None
    ):

        self.name = name
        self.action = action
        self.data = data or {}

        self.priority = priority
        self.depends_on = depends_on or []

        self.status = "Pending"
        self.result = None

        self.created = datetime.now()
        self.started = None
        self.completed = None

    def running(self):

        self.status = "Running"
        self.started = datetime.now()

    def complete(self, result=None):

        self.status = "Completed"
        self.result = result
        self.completed = datetime.now()

    def fail(self, reason=None):

        self.status = "Failed"
        self.result = reason
        self.completed = datetime.now()

    def is_ready(self):

        return len(self.depends_on) == 0

    def to_dict(self):

        return {
            "name": self.name,
            "status": self.status,
            "priority": self.priority,
            "result": self.result,
            "data": self.data,
            "created": str(self.created),
            "started": str(self.started),
            "completed": str(self.completed)
        }

    def __str__(self):

        return f"[{self.status}] ({self.priority}) {self.name}"