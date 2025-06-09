import random

questions = [
    {
        "question": "Which of these is a Python keyword?",
        "options": ["define", "lambda", "func", "returning"],
        "answer": "lambda"
    },
    {
        "question": "What keyword is used to start a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "def"
    },
    {
        "question": "Which keyword is used for a conditional branch?",
        "options": ["when", "if", "check", "else if"],
        "answer": "if"
    },
    {
        "question": "What keyword is used to define a class?",
        "options": ["object", "define", "type", "class"],
        "answer": "class"
    },
    {
        "question": "Which of the following is used to handle exceptions?",
        "options": ["try", "except", "catch", "handle"],
        "answer": "try"
    },
    {
        "question": "What keyword is used to import modules?",
        "options": ["include", "require", "import", "use"],
        "answer": "import"
    },
    {
        "question": "Which keyword is used to create a generator?",
        "options": ["yield", "generate", "return", "pass"],
        "answer": "yield"
    },
    {
        "question": "What keyword is used to declare a loop?",
        "options": ["iterate", "for", "loop", "each"],
        "answer": "for"
    },
    {
        "question": "Which keyword is used to end a function and return a value?",
        "options": ["exit", "break", "return", "stop"],
        "answer": "return"
    },
    {
        "question": "Which of these is used to define a constant block of code?",
        "options": ["const", "block", "with", "static"],
        "answer": "with"
    }
]

def run_quiz():
    print("🧠 Welcome to the Python Keywords Quiz!")
    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"\n{idx}. {q['question']}")
        for i, opt in enumerate(q['options'], 1):
            print(f"   {i}. {opt}")
        
        try:
            choice = int(input("Your answer (1-4): "))
            if q['options'][choice - 1] == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print(f"⚠️ Invalid input. Correct answer: {q['answer']}")

    print(f"\n🏁 Quiz Complete! Your score: {score}/10")

if __name__ == "__main__":
    run_quiz()
