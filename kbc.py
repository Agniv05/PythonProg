# KBC-like Quiz Game in Python

# List of questions, options, and correct answers
questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
        "answer": 2,
        "amount": 1000
    },
    {
        "question": "Who is the author of 'Harry Potter' series?",
        "options": ["1. J.R.R. Tolkien", "2. George R.R. Martin", "3. J.K. Rowling", "4. Stephen King"],
        "answer": 3,
        "amount": 5000
    },
    {
        "question": "What is the capital of France?",
        "options": ["1. Rome", "2. Berlin", "3. Paris", "4. Madrid"],
        "answer": 3,
        "amount": 10000
    },
    {
        "question": "Which gas is essential for respiration?",
        "options": ["1. Nitrogen", "2. Oxygen", "3. Carbon dioxide", "4. Hydrogen"],
        "answer": 2,
        "amount": 50000
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["1. Vincent van Gogh", "2. Leonardo da Vinci", "3. Pablo Picasso", "4. Claude Monet"],
        "answer": 2,
        "amount": 100000
    }
]

# Function to display a question
def ask_question(q):
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = int(input("Enter the option number (1/2/3/4): "))
    return answer == q["answer"], q["amount"]

# Game logic
def play_game():
    total_amount = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1} for ₹{q['amount']}:")
        correct, amount = ask_question(q)
        if correct:
            total_amount += amount
            print(f"Correct! You've won ₹{total_amount} so far.")
        else:
            print("Incorrect! Game over.")
            break
    print(f"\nYou're taking home ₹{total_amount}!")

# Start the game
print("Welcome to KBC!\n")
play_game()
mim = int(input("Enter choice: ")) 