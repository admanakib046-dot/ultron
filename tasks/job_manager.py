from tasks.background_job import BackgroundJob


class JobManager:

    def __init__(self):

        self.jobs = []

    def start(self, workflow, executor):

        job = BackgroundJob(
            workflow,
            executor
        )

        job.start()

        self.jobs.append(job)

        return job

    def list_jobs(self):

        return self.jobs