from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text_value = question["text"]
    anwser_value = question["answer"]
    new_q = Question(text_value, anwser_value)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()