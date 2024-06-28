class User_Input_Memory:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
        # if len(self.questions) >= 10:
        #     self.questions.pop(0)

    def last_questions(self):
        return self.questions
