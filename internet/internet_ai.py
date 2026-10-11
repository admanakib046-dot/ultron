from brain.ai_manager import AIManager


class InternetAI:

    def __init__(self):
        self.ai = AIManager()

    def summarize(self, search_results, question):

        prompt = f"""
You are Ultron.

Answer ONLY using the search results below.

If the answer exists in the search results,
answer it naturally.

Do NOT say:
"I don't know."
"I don't have internet."
"I cannot browse."

Question:
{question}

Search Results:
{search_results}

Answer:
"""

        return self.ai.ask(prompt)