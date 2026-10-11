from brain.nlp import NLP
from memory.memory import Memory
nlp = NLP()
memory = Memory()
while True:
     text = input("You:")
     if text.lower()== "exit":
          break
     intent = nlp.understand(text)
     if intent.action == "remember":
          key =intent.data["key"]
          value =intent.data["value"]
          memory.remember(key,value)
          print(f"Ultron:I'll remember that {key}={value}")
     elif intent.action == "recall":
          key = intent.data ["key"]
          value = memory.recall(key)
          if value:
               print(f"Ultron: {key}={value}")
          else:
               print(f"Ultron:I dont remember this")
     else:
          print(f"Ultron: Ai module isnt connected yet")