#CTI 110 
#
import random

def welcome_user():
    print("Welcome to the history quiz!")
    print("Answer the questions and see how well you do.")

def ask_question(question, choices, correct_answer):
    print(question)
    random.shuffle(choices)  # Randomize the order of choices
    correct_choice = choices.index(correct_answer) + 1
    for idx, choice in enumerate(choices):
        print(f"{idx+1}. {choice}")
    user_answer = input("Please enter your answer (1-{}): ".format(len(choices)))
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == correct_choice:
            print("Correct!")
            return True
    print("Incorrect.")
    return False

def play_quiz():
    score = 0

    welcome_user()

    questions = [
        {"question": "Who was the first President of the United States?", 
         "choices": ["George Washington", "Thomas Jefferson", "John Adams"], 
         "correct_answer": "George Washington"},
        {"question": "Which historical figure is known for writing the 'Declaration of Independence'?", 
         "choices": ["Benjamin Franklin", "Abraham Lincoln", "Thomas Jefferson"], 
         "correct_answer": "Thomas Jefferson"},
        {"question": "Which war lasted from 1914 to 1918?", 
         "choices": ["World War I", "World War II", "Vietnam War"], 
         "correct_answer": "World War I"},
        {"question": "What year did Christopher Columbus discover America?", 
         "choices": ["1492", "1776", "1812"], 
         "correct_answer": "1492"},
        {"question": "Who was the leader of the Soviet Union during World War II?", 
         "choices": ["Joseph Stalin", "Vladimir Lenin", "Mikhail Gorbachev"], 
         "correct_answer": "Joseph Stalin"}
    ]

    for question in questions:
        if ask_question(question["question"], question["choices"], question["correct_answer"]):
            score += 1

    print("Your total score is:", score)

play_quiz()
