from tasks.workflow_builder import WorkflowBuilder
from brain.intent import intent

builder = WorkflowBuilder()

workflow = builder.build(

    intent(
        action="unknown",
        data={
            "goal": "Build Flask website"
        }
    )

)

for task in workflow:

    print(task)