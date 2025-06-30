
class QuestionBrain:

    def __init__(self,  q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

        #GET CURRENT QUESTION:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{str(self.question_number)}: {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer:str, c_answer:str):
        if u_answer.lower() == c_answer.lower():
            print("You got the right answer")
            self.score += 1
        else:
            print("Incorrect Answer!")
        print(f"The expected answer is {c_answer}")
        print(f"Your current score is: {str(self.score)}/{str(self.question_number)}")
        print("\n")


