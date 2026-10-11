from tasks.task import Task


class WorkflowTemplates:

    def build(self, intent):

        action = intent.action

        # ==========================
        # Learn Document
        # ==========================

        if action == "learn":

            file = intent.data["file"]

            return [

                Task(
                    "Read document",
                    "load_file",
                    {"file": file}
                ),

                Task(
                    "Split into chunks",
                    "chunk",
                    {"file": file}
                ),

                Task(
                    "Store knowledge",
                    "knowledge_store",
                    {"file": file}
                )

            ]

        # ==========================
        # Search Knowledge
        # ==========================

        if action == "knowledge_search":

            return [

                Task(
                    "Search knowledge",
                    "knowledge_search",
                    {
                        "query": intent.data["query"]
                    }
                )

            ]

        # ==========================
        # Calculator
        # ==========================

        if action == "calculate":

            return [

                Task(
                    "Calculate expression",
                    "calculate",
                    {
                        "expression":
                        intent.data["expression"]
                    }
                )

            ]

        return []