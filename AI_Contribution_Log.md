# AI Contribution Log

## Project: AI Study Assistant

### AI Tool Used
GitHub Copilot

### Objective
To develop a simple Python-based study assistant using an
AI-assisted coding workflow and to document the contribution
made by the AI tool.

## Contribution Record

| Code Section | AI Contribution | My Action / Verification |
|---|---|---|
| Program comments | Copilot suggested comments describing the purpose of the program. | I reviewed the comments and kept the useful ones. |
| `identify_topic()` | Copilot generated the function structure for identifying the topic of a question. | I reviewed the function and tested it with sample questions. |
| `question.lower()` | Copilot suggested converting the question to lowercase. | I verified that this allows keywords to be detected regardless of capitalization. |
| Programming keywords | Copilot suggested keywords such as Python, Java, code, algorithm and function. | I reviewed the list and kept relevant programming terms. |
| Programming keyword loop | Copilot generated the loop used to compare keywords with the user's question. | I tested it using a Python-related question. |
| Mathematics keywords | Copilot suggested mathematics-related keywords such as algebra, geometry and calculus. | I reviewed the keywords and tested the topic detection. |
| `get_response()` | Copilot suggested a function for producing responses according to the detected topic. | I reviewed the conditional logic and modified the responses. |
| `if / elif / else` | Copilot generated the conditions for selecting the appropriate response. | I checked that each topic produces the expected response. |
| `main()` | Copilot suggested the main program structure. | I reviewed the sequence of input, processing and output. |
| User input | Copilot suggested using `input()` to receive the student's question. | I tested the program with my own question. |
| Topic detection | Copilot connected the user input with `identify_topic()`. | I verified that the question was correctly classified. |
| Final response | Copilot suggested displaying the generated response using `print()`. | I tested the final output in the terminal. |

## Testing

### Test Input
How do I learn Python programming?

### Observed Output
It sounds like a programming question. Try breaking the problem
into smaller steps.

### Result
The program correctly identified the question as a programming
question and displayed the expected response.

## Reflection

GitHub Copilot helped me generate the initial structure and logic
of the Python program. I learned that AI-generated code should not
be accepted without checking it. I reviewed the generated code,
corrected formatting issues, tested the program and documented the
AI contribution. The Contribution Log provides transparency about
the use of AI during development.
## Contribution ID: 001

**File:** agent.py

**AI Tool:** GitHub Copilot

**Prompt:** Create an infinite chatbot loop that takes input from the user.

**AI Contribution:** Copilot modified `agent.py` and created a simple
chatbot REPL with a continuous input loop and exit handling.

**Accepted:** Yes

**Modification:** I reviewed the generated code before testing it.

**Reason:** The loop allows the chatbot to continuously interact with
the user until an exit command is given.

**Verification:** The code will be run in VS Code to check whether the
chatbot accepts user input and exits correctly.