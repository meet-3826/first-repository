# AI Study Assistant
# This program identifies the topic of a student's question
# and provides a simple response.

def identify_topic(question):
    question_lower = question.lower()

    programming_keywords = [
        "code", "programming", "python", "java",
        "debug", "algorithm", "function"
    ]

    for keyword in programming_keywords:
        if keyword in question_lower:
            return "programming"

    math_keywords = [
        "math", "mathematics", "algebra",
        "geometry", "calculus", "equation", "number"
    ]

    for keyword in math_keywords:
        if keyword in question_lower:
            return "mathematics"

    return "general study"


def get_response(topic):
    if topic == "programming":
        return "It sounds like a programming question. Try breaking the problem into smaller steps."

    elif topic == "mathematics":
        return "This seems like a math question. Review the concept and solve it step by step."

    else:
        return "This looks like a general study question. Stay organized and revise your notes regularly."


def main():
    print("Welcome to the AI Study Assistant!")
    print("Ask a question about programming, mathematics, or general study.")

    user_question = input("\nWhat is your question? ")

    topic = identify_topic(user_question)
    response = get_response(topic)

    print("\nAssistant response:")
    print(response)


if __name__ == "__main__":
    main()