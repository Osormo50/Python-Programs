class QuizBrain:

    def __init__(self,lis_q):
        self.list_q = lis_q
        self.q_number = 0
        self.score = 0

    def still_has_questions(self):
        if self.q_number < len(self.list_q):
            return True
        else:
            return False


    def next_question(self):
        current_question = self.list_q[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q{self.q_number}: {current_question.n_questions} (True/False): ")
        self.check_answer(user_answer.lower(),current_question.n_answer.lower())

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct Answer was {correct_answer}")
        print(f"Your current Score is {self.score}/{self.q_number}")
        print("\n")

