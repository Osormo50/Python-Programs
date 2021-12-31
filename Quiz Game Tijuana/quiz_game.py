from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_library = []

for question in question_data:
    new_question = question['question']
    new_answer = question['answer']
    question_library.append(Question(new_question,new_answer))

quiz = QuizBrain(question_library)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your Score was {quiz.score}/{quiz.q_number}")
