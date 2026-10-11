class Reasoner:

    def think(self, intent):

        plan = []

        if intent.action == "search":
            plan.append("Analyze the question")
            plan.append("Choose best search provider")
            plan.append("Search internet")
            plan.append("Summarize results")

        elif intent.action == "calculate":
            plan.append("Parse expression")
            plan.append("Calculate answer")

        elif intent.action == "remember":
            plan.append("Store memory")

        elif intent.action == "recall":
            plan.append("Retrieve memory")

        else:
            plan.append("Ask AI")

        return plan