def chatbot():
    """Simple chatbot REPL.

    - Type messages to interact.
    - Use `exit` or `quit`, or press Ctrl-C / Ctrl-D to stop.
    """
    print("Simple AI agent. Type 'exit' or 'quit' to stop.")
    history = []
    try:
        while True:
            user = input("You: ").strip()
            if not user:
                continue
            if user.lower() in ("exit", "quit"):
                print("Bot: Goodbye!")
                break
            if user.endswith("?"):
                reply = "That's an interesting question."
            else:
                reply = f"I heard: {user}"
            history.append(("User", user))
            history.append(("Bot", reply))
            print("Bot:", reply)
    except (KeyboardInterrupt, EOFError):
        print("\nBot: Goodbye!")


if __name__ == "__main__":
    chatbot()