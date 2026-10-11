from tasks.task import Task


class TaskPlanner:
    def plan(self, intent):
        return self.create_plan(intent.action)

    def create_plan(self, goal):

        goal = goal.lower()

        tasks = []

        if "website" in goal:

            tasks = [
                Task("Choose Framework", "research", priority=10),
                Task("Design UI", "design", priority=9),
                Task("Build Backend", "backend", priority=8),
                Task("Connect Database", "database", priority=7),
                Task("Testing", "testing", priority=6),
                Task("Deployment", "deploy", priority=5)
            ]

        elif "ai assistant" in goal or "ultron" in goal:

            tasks = [
                Task("Speech Recognition", "speech", priority=10),
                Task("Vision System", "vision", priority=9),
                Task("Memory System", "memory", priority=8),
                Task("Planning System", "planning", priority=7),
                Task("Decision Engine", "decision", priority=6),
                Task("Automation", "automation", priority=5),
                Task("GUI", "gui", priority=4)
            ]

        elif "study" in goal:

            tasks = [
                Task("Read Notes", "study", priority=10),
                Task("Practice Questions", "practice", priority=9),
                Task("Take Quiz", "quiz", priority=8),
                Task("Review Mistakes", "review", priority=7)
            ]

        else:

            tasks = [
                Task("Analyze Goal", "analyze", priority=10),
                Task("Break Into Subtasks", "plan", priority=9),
                Task("Execute Tasks", "execute", priority=8),
                Task("Review Progress", "review", priority=7)
            ]

        return tasks