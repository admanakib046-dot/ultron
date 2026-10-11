from tasks.workflow_builder import WorkflowBuilder
from brain.intent import intent

builder = WorkflowBuilder()

workflow = builder.build(

    intent(
        action="create_flask",
        data={}
    )

)

for task in workflow:

    print(task)