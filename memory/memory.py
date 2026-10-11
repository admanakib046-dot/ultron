import json
import os
from datetime import datetime


class Memory:

    def __init__(self):
        self.file = "memory/memory.json"
        self.memory = {}
        self.load()

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.memory = json.load(f)

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def remember(self, key, value, category="general", importance=5):

        # Update existing memory
        if key in self.memory:
            self.memory[key]["value"] = value
            self.memory[key]["updated"] = datetime.now().isoformat()
            self.memory[key]["last_used"] = datetime.now().isoformat()

        # Create new memory
        else:
            self.memory[key] = {
                "value": value,
                "category": category,
                "importance": importance,
                "created": datetime.now().isoformat(),
                "updated": datetime.now().isoformat(),
                "last_used": datetime.now().isoformat()
            }

        self.save()

    def recall(self, key):

      if key not in self.memory:
        return None

      self.memory[key]["last_used"] = datetime.now().isoformat()
      self.save()

      return self.memory[key]

    def forget(self, key):

        if key in self.memory:
            del self.memory[key]
            self.save()

    def search(self, text):

        results = {}

        text = text.lower()

        for key, info in self.memory.items():

            if text in key.lower():

                results[key] = info

            elif text in str(info["value"]).lower():

                results[key] = info

        return results
    def stats(self):
        return {
        "total_memories": len(self.memory),
        "categories": list(set(
            item["category"]
            for item in self.memory.values()
        ))
    }

    def all(self):
        return self.memory