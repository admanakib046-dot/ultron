from brain.nlp import NLP
from brain.router import router

nlp = NLP()
router = router()

while True:
    text = input("You:")
    if text.lower() == "exit":
        break
    intent =nlp.understand(text)
    destination = router.route(intent)

    print("Intent:",intent.action)
    print("route:",destination)