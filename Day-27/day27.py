# Kaun Banega Crorepati
# Question --> Create A Program Of Question And Answers
import random

# Define a list of questions, each question is a tuple of (question_text, options, correct_answer)
questions = [
    ("What is the capital of France?", ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"], "A"),
    ("Which planet is known as the Red Planet?", ["A. Mars", "B. Jupiter", "C. Saturn", "D. Venus"], "A"),
    ("Who wrote 'Romeo and Juliet'?", ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"], "A"),
    # Add more questions here
]

def ask_question(question, options):
    print(question)
    for option in options:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").upper()
    return answer

def kbc_game():
    random.shuffle(questions)
    total_questions = len(questions)
    correct_answers = 0
    
    print("Welcome to Kaun Banega Crorepati!")
    print("You'll be asked", total_questions, "questions. Let's begin:")
    print()
    
    for i, (question, options, correct_answer) in enumerate(questions, start=1):
        print("Question", i)
        user_answer = ask_question(question, options)
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect! The correct answer was:", correct_answer)
        print()
    
    print("Game Over!")
    print("You answered", correct_answers, "out of", total_questions, "questions correctly.")

kbc_game()
