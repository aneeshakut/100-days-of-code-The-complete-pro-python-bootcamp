#Quiz Game

import random

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_option

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.display_question()
            user_answer = int(input("Enter your answer (1, 2, 3, or 4): "))
            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}: {question.options[question.correct_option - 1]}\n")
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

questions = [
    Question("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 1),
    Question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus", "Saturn"], 1),
    Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2),
    Question("In which year did World War II end?", ["1943", "1944", "1945", "1946"], 3),
    Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2),
    Question("What is the currency of Japan?", ["Won", "Yuan", "Yen", "Ringgit"], 3),
    Question("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Silver", "Iron"], 1),
    Question("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "South Korea", "Vietnam"], 2),
    Question("What is the square root of 144?", ["10", "12", "14", "16"], 2),
    Question("Who is known as the 'Father of Computers'?", ["Alan Turing", "Charles Babbage", "Ada Lovelace", "John von Neumann"], 2),
]

quiz = Quiz(questions)
quiz.start_quiz()
