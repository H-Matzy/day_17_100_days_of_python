import data
class Question:
    def __init__(self, text, answer, category):
        self.text = text
        self.answer = answer
        self.category = category

    def grade(self):
        print(f'Answer was {self.answer}, you answered {self.answer}')
        print(f'You were {self.text == self.answer}')




