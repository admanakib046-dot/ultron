from tasks.task import Task


class DynamicPlanner:

    def create_plan(self, intent):

        action = intent.action.lower()

        tasks = []

        # ==========================
        # Flask Project
        # ==========================

        if action == "create_flask":

            tasks.append(
                Task(
                    "Create Project Folder",
                    "create_folder"
                )
            )

            tasks.append(
                Task(
                    "Generate app.py",
                    "generate_file"
                )
            )

            tasks.append(
                Task(
                    "Generate templates",
                    "generate_templates"
                )
            )

            tasks.append(
                Task(
                    "Install Flask",
                    "install_package"
                )
            )

            tasks.append(
                Task(
                    "Run Server",
                    "run_server"
                )
            )

            return tasks

        # ==========================
        # Default
        # ==========================

        return []