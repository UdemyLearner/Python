from questions_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank  = []

for ques in question_data:
    ques_text = ques["question"]
    ques_ans = ques["correct_answer"]
    new_question = Question(ques_text,ques_ans)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.nxt_question()
    
print(f"quiz was completed and your final score was {quiz.score}")