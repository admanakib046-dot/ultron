class TaskQueue:

    def __init__(self):

        self.pending = []
        self.running = []
        self.completed = []
        self.failed = []

    # -------------------------
    # Add Task
    # -------------------------

    def add_task(self, task):

        self.pending.append(task)

        self.pending.sort(
            key=lambda t: t.priority,
            reverse=True
        )

    # -------------------------
    # Get Next Task
    # -------------------------

    def next_task(self):

        if not self.pending:
            return None

        task = self.pending.pop(0)

        task.running()

        self.running.append(task)

        return task

    # -------------------------
    # Complete Task
    # -------------------------

    def complete_task(self, task, result=None):

        if task in self.running:

            self.running.remove(task)

            task.complete(result)

            self.completed.append(task)

    # -------------------------
    # Fail Task
    # -------------------------

    def fail_task(self, task, reason=None):

        if task in self.running:

            self.running.remove(task)

            task.fail(reason)

            self.failed.append(task)

    # -------------------------
    # Pending
    # -------------------------

    def pending_tasks(self):

        return self.pending

    # -------------------------
    # Running
    # -------------------------

    def running_tasks(self):

        return self.running

    # -------------------------
    # Completed
    # -------------------------

    def completed_tasks(self):

        return self.completed

    # -------------------------
    # Failed
    # -------------------------

    def failed_tasks(self):

        return self.failed

    # -------------------------
    # Queue Status
    # -------------------------

    def status(self):

        return {
            "pending": len(self.pending),
            "running": len(self.running),
            "completed": len(self.completed),
            "failed": len(self.failed)
        }
        # -------------------------
    # Compatibility Methods
    # -------------------------

    def add(self, task):
        self.add_task(task)

    def next(self):
        return self.next_task()

    def empty(self):
        return len(self.pending) == 0

    def clear(self):
        self.pending.clear()
        self.running.clear()
        self.completed.clear()
        self.failed.clear()