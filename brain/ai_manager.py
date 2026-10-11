from config import AI_PROVIDER

from brain.local_ai import LocalAI
from brain.openai_ai import OpenAIAI

class AIManager:
    def __init__(self):
        self.local = LocalAI()
        self.openai = OpenAIAI()
    
    def ask(self, prompt):

     if AI_PROVIDER == "local":
        return self.local.ask(prompt)

     elif AI_PROVIDER == "openai":
        return self.openai.ask(prompt)

     elif AI_PROVIDER == "auto":

        # For now, use Local AI by default
        return self.local.ask(prompt)

     else:
        return "Unknown AI provider."
            