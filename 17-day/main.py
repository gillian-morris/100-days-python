# Day 17 - Quiz Project
# Learning how to write OOP, classes, methods, constructors, attributes

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q_new = Question(item["question"], item["correct_answer"])
    question_bank.append(q_new)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
