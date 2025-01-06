import random

# Questions and answers
questions = [
    {
        'question': 'Which programming language is primarily used for development in Python?',
        'options': ['C', 'Python', 'Java', 'C++'],
        'correct_option': 2  # Python is the correct answer
    },
    {
        'question': 'What is a variable?',
        'options': ['Data type', 'Container for data', 'Operation with data', 'Loop'],
        'correct_option': 2  # Container for data is the correct answer
    }
]

score = 0  # Initial score

# Quiz process
for question in questions:
    print(f"Question: {question['question']}")
    print()  # Adding a space between the question and options

    # Shuffle answer options
    options = question['options'][:]
    random.shuffle(options)
    
    # Print shuffled options
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    print()  # Adding a space between options and input field

    # Find the index of the correct option in the shuffled list
    correct_option_index = options.index(question['options'][question['correct_option'] - 1]) + 1
    
    answer = input("Choose the number of your answer: ")

    if int(answer) == correct_option_index:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print()  # Adding a space after the answer for better readability

# Final results
print(f"\nYou answered {score} out of {len(questions)} questions correctly.")
