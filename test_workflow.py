from tasks.workflow_builder import WorkflowBuilder
from brain.intent import intent

builder = WorkflowBuilder()

workflow = builder.build(

    intent(
        action="learn",
        data={
            "file": "test.txt"
        }
    )

)

print(workflow)

for task in workflow:

    print(task)