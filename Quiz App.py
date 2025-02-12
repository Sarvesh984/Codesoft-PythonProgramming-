import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz App")
        self.quizzes = {
            "Quiz 1": [
                {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "correct": 0},
                {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Saturn", "Jupiter", "Uranus"], "correct": 2},
                {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"], "correct": 0},
            ],
            "Quiz 2": [
                {"question": "What is the smallest country in the world?", "options": ["Vatican City", "Monaco", "Nauru", "Tuvalu"], "correct": 0},
                {"question": "What is the largest living species of lizard?", "options": ["Komodo dragon", "Saltwater crocodile", "Black mamba", "African elephant"], "correct": 0},
                {"question": "Who wrote the famous novel 'To Kill a Mockingbird'?", "options": ["F. Scott Fitzgerald", "Harper Lee", "Jane Austen", "J.K. Rowling"], "correct": 1},
            ],
        }
        self.current_quiz = None
        self.current_question = None
        self.score = 0
        self.home_screen()

    def home_screen(self):
        tk.Label(self.root, text="Available Quizzes:").pack()
        for quiz in self.quizzes:
            tk.Button(self.root, text=quiz, command=lambda quiz=quiz: self.start_quiz(quiz)).pack()
        tk.Button(self.root, text="Start Random Quiz", command=self.start_random_quiz).pack()

    def start_quiz(self, quiz):
        self.current_quiz = quiz
        self.current_question = 0
        self.score = 0
        self.quiz_screen()

    def start_random_quiz(self):
        self.current_quiz = random.choice(list(self.quizzes.keys()))
        self.current_question = 0
        self.score = 0
        self.quiz_screen()

    def quiz_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=self.current_quiz).pack()
        tk.Label(self.root, text=self.quizzes[self.current_quiz][self.current_question]["question"]).pack()
        self.options = self.quizzes[self.current_quiz][self.current_question]["options"]
        self.correct = self.quizzes[self.current_quiz][self.current_question]["correct"]
        self.answer = tk.StringVar()
        for option in self.options:
            tk.Radiobutton(self.root, text=option, variable=self.answer, value=option).pack()
        tk.Button(self.root, text="Submit Answer", command=self.check_answer).pack()

    def check_answer(self):
        if self.answer.get() == self.options[self.correct]:
            self.score += 1
        self.current_question += 1
        if self.current_question < len(self.quizzes[self.current_quiz]):
            self.quiz_screen()
        else:
            self.result_screen()

    def result_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Quiz Complete!").pack()
        tk.Label(self.root, text=f"Your score is {self.score} out of {len(self.quizzes[self.current_quiz])}").pack()
        for i, question in enumerate(self.quizzes[self.current_quiz]):
            tk.Label(self.root, text=f"Question {i+1}: {question['question']}").pack()
            tk.Label(self.root, text=f"Correct answer: {question['options'][question['correct']]}").pack()
            if i < self.score:
                tk.Label(self.root, text="Correct!").pack()
            else:
                tk.Label(self.root, text="Incorrect").pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QuizApp()
    app.run()
