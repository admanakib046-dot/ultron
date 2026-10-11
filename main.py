from brain.thinking import Thinking

def main():
    print("=" * 60)
    print("        Ultron v1.0.1")
    print("=" * 60)
    print('Type "exit" to quit.\n')

    ultron = Thinking()

    while True:
        command = input("You: ")

        if command.lower() == "exit":
            print("Ultron: Goodbye")
            break

        response = ultron.process(command)
        print("Ultron:", response)


if __name__ == "__main__":
    main()
    