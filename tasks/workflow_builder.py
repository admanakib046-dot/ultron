from tasks.workflow_templates import WorkflowTemplates
from tasks.dynamic_planner import DynamicPlanner
from tasks.goal_planner import GoalPlanner


class WorkflowBuilder:

    def __init__(self):

        self.templates = WorkflowTemplates()
        self.dynamic = DynamicPlanner()
        self.goal = GoalPlanner()

    def build(self, intent):

     workflow = self.templates.build(intent)

     if workflow:
        return workflow

     workflow = self.dynamic.create_plan(intent)

     if workflow:
        return workflow

    # Last fallback: goal planning
     return self.goal.plan(
        str(intent.data)
    )