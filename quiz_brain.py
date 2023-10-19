import html
class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def has_more_questions(self):
        return len(self.question_list) >= self.question_number + 1
    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = html.unescape(current_question.text)
        self.question_number += 1
        current_answer = current_question.answer
        print(f"Category: {current_question.category}")
        answer_input = input(f'Q.{self.question_number}: {question_text} (True/False)?\n')
        if answer_input == current_answer:
            self.score += 1
            print("Correct!\n")
        else:
            print("Sorry, that was incorrect...\n")