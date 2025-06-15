def run_quiz(questions):
    score = 0

    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        if answer == question["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was {question['answer']}.")

    print("\nQuiz Over!")
    print(f"Your final score is: {score}/{len(questions)}")

# List of questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which number is a prime number?",
        "options": ["A. 9", "B. 11", "C. 15", "D. 21"],
        "answer": "B"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["A. 30", "B. 20", "C. 25", "D. 35"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 8", "C. 10", "D. 12"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A. 90°C", "B. 95°C", "C. 100°C", "D. 105°C"],
        "answer": "C"
    },
    {
        "question": "Which gas do plants use for photosynthesis?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Hydrogen", "D. Carbon Dioxide"],
        "answer": "D"
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "options": ["A. Asia", "B. Africa", "C. Australia", "D. South America"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Go", "C. Au", "D. Gd"],
        "answer": "C"
    },
    {
        "question": "Which animal is known as the 'King of the Jungle'?",
        "options": ["A. Elephant", "B. Tiger", "C. Lion", "D. Gorilla"],
        "answer": "C"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": ["A. 365", "B. 366", "C. 364", "D. 367"],
        "answer": "B"
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["A. Hydrogen", "B. Salt", "C. Water", "D. Oxygen"],
        "answer": "C"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which programming language is this quiz written in?",
        "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
        "answer": "B"
    }
]

# Run the quiz
run_quiz(quiz_questions)
