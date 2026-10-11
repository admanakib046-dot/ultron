class KnowledgeContext:

    def build(self, conversation_context, knowledge):

        prompt = ""

        # ==========================
        # Conversation Context
        # ==========================

        prompt += conversation_context

        # ==========================
        # Knowledge Context
        # ==========================

        if knowledge:

            prompt += "\n\n"
            prompt += "=" * 60
            prompt += "\nKNOWLEDGE\n"
            prompt += "=" * 60
            prompt += "\n"

            if isinstance(knowledge, list):

                for item in knowledge:
                    prompt += item
                    prompt += "\n\n"

            else:
                prompt += str(knowledge)

            prompt += "\n"
            prompt += "=" * 60
            prompt += "\n"

        # ==========================
        # Final Instruction
        # ==========================

        prompt += """

Use the knowledge above if it is relevant.
If the knowledge is unrelated, ignore it.
Never invent facts that are not present in the knowledge.
"""

        return prompt