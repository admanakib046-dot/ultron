from brain.decision import Decision

decision = Decision()

tests = [

    ("memory", "remember my name"),
    ("internet", "who is Elon Musk"),
    ("weather", "weather today"),
    ("tool", "calculate 10+5"),
    ("news", "latest AI news"),
    ("ai", "look at this image"),
    ("ai", "read this pdf"),
    ("ai", "build a website"),
    ("ai", "tell me a joke")

]

for planner_result, command in tests:

    result = decision.decide(planner_result, command)

    print("--------------------------------")
    print("Command :", command)
    print("Decision:", result)
    print(decision.explain(result))