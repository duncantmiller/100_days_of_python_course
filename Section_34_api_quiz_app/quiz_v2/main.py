"""import Question, question data and QuizBrain"""

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from ui import QuizInterface

question_bank = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print(f"You scored {quiz.score()}")
