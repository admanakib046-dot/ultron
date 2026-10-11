from tasks.task import Task


class GoalPlanner:

    def plan(self, goal):

        goal = goal.lower()

        tasks = []

        if "flask" in goal:

            tasks.extend([

                Task(
                    "Create Project",
                    "create_folder"
                ),

                Task(
                    "Generate Flask App",
                    "generate_file"
                ),

                Task(
                    "Install Flask",
                    "install_package"
                ),

                Task(
                    "Run Server",
                    "run_server"
                )

            ])

        elif "website" in goal:

            tasks.extend([

                Task(
                    "Create HTML",
                    "generate_html"
                ),

                Task(
                    "Create CSS",
                    "generate_css"
                ),

                Task(
                    "Create JavaScript",
                    "generate_js"
                )

            ])

        return tasks