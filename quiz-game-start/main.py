from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain

#list of Question
question_bank = []

#iterate through question_data and convert each dictionary to Question type
for q_dict in question_data:
    #create new Question object
    text = q_dict["text"]
    answer = q_dict["answer"]
    #append new Question object to question_bank
    question_bank.append(Question(text, answer))

quiz_engine = QuestionBrain(question_bank)

while quiz_engine.still_has_questions():
    quiz_engine.next_question()

print("Quiz Completed!")
print(f"You scored {str(quiz_engine.score)}/{str(quiz_engine.question_number)}")
