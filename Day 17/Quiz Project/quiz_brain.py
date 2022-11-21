class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def nxt_question(self):
        current_ques = self.question_list[self.question_number]
        self.question_number += 1
        u_ans = input(f"Q.{self.question_number} {current_ques.text} (True/False) :")
        self.check_ans(u_ans, current_ques.answer)

    def check_ans(self, u_ans, ans):
        if u_ans.lower() == ans.lower():
            self.score += 1
            print("correct ans")
        else:
            print("wrong ans")
        print(f"correct ans was {ans}")
        print(f"correct score is {self.score}/{self.question_number}")
        print("\n")
