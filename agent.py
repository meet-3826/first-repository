def chatbot():
    """Simple chatbot REPL.

    - Type messages to interact.
    - Use `exit` or `quit`, or press Ctrl-C / Ctrl-D to stop.
    """
    print("Simple AI agent. Type 'exit' or 'quit' to stop.")
    history = []

    PREDEFINED_RESPONSES = [
        (
            ["ai", "artificial intelligence", "what is ai", "what is artificial intelligence", "how does ai"],
            (
                "AI stands for artificial intelligence. "
                "It's about building systems that can perform tasks that normally require human intelligence, "
                "like recognizing patterns, understanding language, and making decisions. Start with basic ML concepts."
            ),
        ),
        (
            ["python", "what is python", "learn python", "how to learn python"],
            (
                "Python is a beginner-friendly, high-level programming language. "
                "It has simple syntax, a large standard library, and many learning resources. "
                "Try small projects and practice frequently."
            ),
        ),
        (
            ["git", "version control", "what is git", "commit", "push", "pull", "clone"],
            (
                "Git is a distributed version control system. "
                "Use it to track changes, collaborate, and manage code history. "
                "Common commands: `git init`, `git add`, `git commit`, `git push`, `git pull`."
            ),
        ),
        (
            ["c language", "c programming", "what is c", "compile c", "gcc"],
            (
                "C is a low-level, compiled programming language often used for systems programming. "
                "You write code, compile it with a compiler like `gcc`, and run the produced executable. "
                "It's great for learning how memory and pointers work."
            ),
        ),
        (
            ["data structure","what is data structures",  "data structures", "algorithm", "algorithms", "big o", "sorting", "searching"],
            (
                "Data structures store and organize data (arrays, lists, trees, hash tables). "
                "Algorithms are step-by-step procedures to solve problems (sorting, searching). "
                "Learn common structures and practice algorithmic thinking with small problems."
            ),
        ),
    ]
    try:
        while True:
            user = input("You: ").strip()
            if not user:
                continue
            if user.lower() in ("exit", "quit"):
                print("Bot: Goodbye!")
                break

            # Rule-based predefined responses for common beginner topics
            user_lower = user.lower()
            reply = None
            for keywords, text in PREDEFINED_RESPONSES:
                if any(k in user_lower for k in keywords):
                    reply = text
                    break

            # Fallback behavior if no predefined reply matched
            if reply is None:
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
