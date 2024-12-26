from .data import question_data
from .question_model import Question
from .quiz_brain import QuizBrain
from common_functions import typing, hold_screen, clear_screen

question_bank = []
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    clear_screen()
    quiz.next_question()
    hold_screen()

typing("\nYou've Completed the Quiz!!")
typing(f"Your Final Score is {quiz.score}/{quiz.question_number}.\n")