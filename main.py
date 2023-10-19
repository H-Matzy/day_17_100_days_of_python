from fetch_questions import fetch_quiz_questions
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

question_data = fetch_quiz_questions(10)
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    category = item["category"]
    question_bank.append(Question(text, answer, category))

quiz = QuizBrain(question_bank)
while quiz.has_more_questions():
    quiz.next_question()
print(f'Quiz Complete! You have scored a {quiz.score}/{len(quiz.question_list)}')
