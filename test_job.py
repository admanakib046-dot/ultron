
from brain.thinking import Thinking

from tasks.workflow_builder import WorkflowBuilder
from tasks.task_executor import TaskExecutor
from tasks.job_manager import JobManager

from brain.intent import intent


# Create the real Ultron brain
thinking = Thinking()

# Task Engine
builder = WorkflowBuilder()
executor = TaskExecutor(thinking)
manager = JobManager()

# Build a workflow
workflow = builder.build(

    intent(
        action="calculate",
        data={
            "expression": "5+5"
        }
    )

)

# Start background job
job = manager.start(
    workflow,
    executor
)

# Wait until finished
job.join()

# Print status
print("\nJob Status:", job.status)