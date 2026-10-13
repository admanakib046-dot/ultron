from brain.ai_manager import AIManager
from brain.nlp import NLP
from brain.planner import planner
from brain.router import router
from brain.reasoner import Reasoner
from brain.decision import DecisionEngine
from brain.fallback import FallbackEngine
from brain.context import ContextBuilder

from memory.memory import Memory
from memory.conversation import ConversationMemory
from memory.memory_detector import MemoryDetector

from tools.tools_manager import ToolsManager

from internet.internet_manager import InternetManager
from internet.internet_ai import InternetAI

from knowledge.search import KnowledgeSearch
from knowledge.context import KnowledgeContext

from logs.logger import Logger

from plugin.plugin_manager import PluginManager

from core.services import Services

from updater.update_manager import UpdateManager
from updater.evolution import Evolution

from tasks.task_planner import TaskPlanner
from tasks.task_queue import TaskQueue
from tasks.task_executor import TaskExecutor


class Thinking:

    def __init__(self):

        # ==========================
        # Core
        # ==========================
        self.ai_manager = AIManager()
        self.nlp = NLP()
        self.planner = planner()
        self.router = router()
        self.reasoner = Reasoner()
        self.decision = DecisionEngine()
        self.fallback = FallbackEngine()

        # ==========================
        # Memory
        # ==========================
        self.memory = Memory()
        self.memory_detector = MemoryDetector()
        self.conversation = ConversationMemory()

        # ==========================
        # Tools
        # ==========================
        self.tools = ToolsManager()

        # ==========================
        # Task Engine
        # ==========================
        self.task_planner = TaskPlanner()
        self.task_queue = TaskQueue()
        self.task_executor = TaskExecutor()

        # ==========================
        # Context
        # ==========================
        self.context = ContextBuilder(self.memory, self.conversation)

        # ==========================
        # Internet
        # ==========================
        self.internet = InternetManager()
        self.internet_ai = InternetAI()

        # ==========================
        # Knowledge
        # ==========================
        self.knowledge_search = KnowledgeSearch()
        self.knowledge_context = KnowledgeContext()

        # ==========================
        # Logger
        # ==========================
        self.logger = Logger()

        # ==========================
        # Updater / Evolution
        # ==========================
        self.updater = UpdateManager()
        self.evolution = Evolution()

        # ==========================
        # Services
        # ==========================
        self.services = Services()
        self.services.add("memory", self.memory)
        self.services.add("conversation", self.conversation)
        self.services.add("tools", self.tools)
        self.services.add("internet", self.internet)
        self.services.add("logger", self.logger)
        self.services.add("ai", self.ai_manager)
        self.services.add("reasoner", self.reasoner)
        self.services.add("context", self.context)

        # ==========================
        # Plugins
        # ==========================
        self.plugins = PluginManager()
        self.plugins.load_plugins(self.services)

    def process(self, command):

        cmd = command.strip().lower()

        # ==========================
        # Plugins
        # ==========================
        if cmd == "plugins":
            return "\n".join(self.plugins.list_plugins())

        # ==========================
        # Updates
        # ==========================
        if cmd == "check updates":

         info = self.updater.check()

         if not info:
          return "Unable to contact GitHub."

         if not info["update"]:
          return (
          "Ultron is already up to date.\n\n"
          f"Current Version: {info['current']}"
    )

         return (
        f"Current Version : {info['current']}\n\n"
        f"Latest Version : {info['latest']}\n\n"
        f"{info['notes']}\n\n"
        "Type:\ninstall update"
    )

        if cmd == "install update":
            ok = self.updater.install()

            if ok:
                return "Ultron updated successfully."

            return "Update failed."

        # ==========================
        # Self Evolution
        # ==========================
        if cmd == "become smarter":
            updates = self.evolution.analyze()

            if not updates:
                return "I couldn't find any improvements."

            text = "I found these improvements:\n\n"

            for u in updates:
                text += (
                    f"• {u['module']} ({u['version']})\n"
                    f"  {u['reason']}\n\n"
                )

            text += "\nType: evolve"
            return text

        # ==========================
        # Install Evolution
        # ==========================
        if cmd == "evolve":
            ok = self.evolution.install()

            if ok:
                return "Evolution completed successfully."

            return "Evolution failed."

        # ==========================
        # Log User
        # ==========================
        self.logger.log("USER", command)

        # ==========================
        # Auto Memory Detection
        # ==========================
        if self.memory_detector.should_remember(command):
            print("\nAUTO MEMORY DETECTED")

        # ==========================
        # NLP + Reasoning
        # ==========================
        intent = self.nlp.understand(command)
        plan = self.reasoner.think(intent)

        # ==========================
        # Decision Engine
        # ==========================
        decision = self.decision.decide(intent.action, command)

        destination = decision.get("destination", "ai")
        reason = decision.get("reason", "No reason given")
        confidence = decision.get("confidence", 0.0)

        # Low confidence -> don't trust the route, let the AI handle it
        MIN_CONFIDENCE = 0.5
        if confidence < MIN_CONFIDENCE and destination != "ai":
            reason = f"{reason} (low confidence, fell back to ai)"
            destination = "ai"

        self.logger.log(
            "DECISION",
            f"{destination} | {confidence} | {reason}"
        )

        # ==========================
        # Debug Output
        # ==========================
        print("\nPLAN")
        for step in plan:
            print("-", step)

        print("=" * 60)
        print("COMMAND      :", command)
        print("ACTION       :", intent.action)
        print("DESTINATION  :", destination)
        print("REASON       :", reason)
        print("CONFIDENCE   :", confidence)
        print("=" * 60)

        # ==========================
        # Save Conversation (user)
        # ==========================
        self.conversation.add("User", command)

        # ==========================
        # Execute Decision
        # ==========================
        if destination == "internet":
            answer = self.internet.search(command)

        elif destination == "memory":
            answer = self.memory.search(command)

        elif destination == "vision":
            answer = "Vision module not implemented yet."

        elif destination == "document":
            answer = "Document module not implemented yet."

        elif destination == "task":
            tasks = self.task_planner.create_plan(command)

            for task in tasks:
                print(task)
                self.task_queue.add_task(task)

            while self.task_queue.pending_tasks():
                task = self.task_queue.next_task()
                result = self.task_executor.execute(task)
                self.task_queue.complete_task(task, result)

            answer = "Task completed."

        else:
            # AI
            results = self.knowledge_search.search(command)

            if results:
                print("\nKNOWLEDGE FOUND")
                prompt = self.knowledge_context.build(command, results)
                answer = self.ai_manager.ask(prompt)
            else:
                answer = self.ai_manager.ask(command)

        # ==========================
        # Log AI
        # ==========================
        self.logger.log("AI", answer)

        # ==========================
        # Save Conversation (assistant)
        # ==========================
        self.conversation.add("Ultron", answer)

        return answer