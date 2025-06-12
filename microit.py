import random
import time

def run_quiz(questions):
    """
    Runs the main quiz game.
    """
    score = 0
    total_questions = len(questions)
    user_answers = [] # To store user's choices for review

    print("Welcome to the Python Quiz Game!\n")
    print("Answer the following multiple-choice questions.\n")

    # Shuffle questions to make each game unique
    random.shuffle(questions)

    for i, q in enumerate(questions):
        print(f"\n--- Question {i + 1}/{total_questions} ---")
        print(f"Topic: {q['category']}") # Display category
        print(q['question'])

        # Display shuffled choices
        choices = q['choices']
        random.shuffle(choices) # Shuffle choices for each question
        choice_map = {} # Map choice letter to actual choice
        for j, choice in enumerate(choices):
            choice_letter = chr(65 + j) # A, B, C, D
            choice_map[choice_letter] = choice
            print(f"{choice_letter}. {choice}")

        start_time = time.time() # Start timer for the question
        while True:
            user_input = input("Your answer (A, B, C, D): ").strip().upper()
            if user_input in choice_map:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        end_time = time.time() # End timer for the question
        time_taken = round(end_time - start_time, 2)

        selected_answer = choice_map[user_input]
        is_correct = (selected_answer == q['answer'])
        user_answers.append({
            'question': q['question'],
            'user_choice': selected_answer,
            'correct_answer': q['answer'],
            'is_correct': is_correct,
            'time_taken': time_taken
        })

        if is_correct:
            print(f"Correct! 🎉 (Time taken: {time_taken} seconds)")
            score += 1
        else:
            print(f"Incorrect. 🙁 The correct answer was: {q['answer']} (Time taken: {time_taken} seconds)")

    # --- Quiz End and Feedback ---
    print("\n--- Quiz Finished! ---")
    print(f"You answered {score} out of {total_questions} questions correctly.")
    print(f"Your final score is: {score}/{total_questions}")

    # --- Answer Review ---
    print("\n--- Review Your Answers ---")
    for i, result in enumerate(user_answers):
        status = "Correct" if result['is_correct'] else "Incorrect"
        print(f"\nQuestion {i + 1}: {result['question']}")
        print(f"  Your answer: {result['user_choice']} ({status})")
        if not result['is_correct']:
            print(f"  Correct answer: {result['correct_answer']}")
        print(f"  Time taken: {result['time_taken']} seconds")

def main():
    """
    Defines the quiz questions and starts the game.
    """
    # Define your quiz questions
    # Each question is a dictionary with 'question', 'choices', 'answer', and 'category'
    questions_data = [
        {
            'question': "What is the capital of France?",
            'choices': ["Berlin", "Madrid", "Paris", "Rome"],
            'answer': "Paris",
            'category': "Geography"
        },
        {
            'question': "Which planet is known as the 'Red Planet'?",
            'choices': ["Earth", "Mars", "Jupiter", "Venus"],
            'answer': "Mars",
            'category': "Science"
        },
        {
            'question': "Who painted the Mona Lisa?",
            'choices': ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
            'answer': "Leonardo da Vinci",
            'category': "Art"
        },
        {
            'question': "What is the largest ocean on Earth?",
            'choices': ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            'answer': "Pacific Ocean",
            'category': "Geography"
        },
        {
            'question': "What is the chemical symbol for water?",
            'choices': ["O2", "H2O", "CO2", "NACL"],
            'answer': "H2O",
            'category': "Science"
        },
        {
            'question': "Which animal lays the largest eggs?",
            'choices': ["Eagle", "Ostrich", "Hummingbird", "Chicken"],
            'answer': "Ostrich",
            'category': "Biology"
        },
        {
            'question': "What is the highest mountain in the world?",
            'choices': ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"],
            'answer': "Mount Everest",
            'category': "Geography"
        }
    ]

    run_quiz(questions_data)

if __name__ == "__main__":
    main()
