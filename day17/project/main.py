from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for val in question_data:
    question_bank.append(Question(val["question"], val["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"You've final score was: {quiz.score}/{quiz.question_number}.")
