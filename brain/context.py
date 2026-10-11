from brain.personality import SYSTEM_PROMPT


class ContextBuilder:

    def __init__(self, memory, conversation):
        self.memory = memory
        self.conversation = conversation

    def build(self, command):

        # Long-term memory
        memory = self.memory.all()

        # Recent conversation
        history = self.conversation.get_recent()

        return f"""
{SYSTEM_PROMPT}

=========================
LONG TERM MEMORY
=========================
{memory}

=========================
RECENT CONVERSATION
=========================
{history}

=========================
USER
=========================
{command}

Ultron:
"""

