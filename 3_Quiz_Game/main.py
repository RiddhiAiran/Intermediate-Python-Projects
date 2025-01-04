from .data import question_data, logo
from .question_model import Question
from .quiz_brain import QuizBrain
from common_functions import typing, hold_screen, clear_screen

question_bank = []
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))


quiz = QuizBrain(question_bank)


clear_screen()
typing("Welcome To the Quiz Game! 📄\n")
typing("Ready for The Quiz...📚\n")
hold_screen()
while quiz.still_has_questions():
    clear_screen()
    print(logo)
    quiz.next_question()
    hold_screen()

typing("\nYou've Completed the Quiz!!\n")
typing(f"Your Final Score is {quiz.score}/{quiz.question_number}.\n")