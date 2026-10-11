from brain.ai import AI
class OpenAIAI(AI):
    def ask(self,prompt):
        return f"[OPENAI]\nI received: {prompt}\n(OpenAI not connected yet.)"