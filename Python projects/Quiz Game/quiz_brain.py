class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        currQuestion = self.question_list[self.question_number]
        self.question_number += 1
        user_anwser = input(f"Q.{self.question_number}: {currQuestion.text} (True or False): ")
        self.check_anwser(user_anwser, currQuestion.answer)

    def check_anwser(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("Wrong")
        print(f"The anwser was {correct_answer}, your score is {self.score}. ")