import tkinter as tk
from tkinter import messagebox

def save_question():
    question_text = entry_question.get().strip()
    choice_alpha = entry_alpha.get().strip()
    choice_bravo = entry_bravo.get().strip()
    choice_charlie = entry_charlie.get().strip()
    choice_delta = entry_delta.get().strip()
    correct_answer = correct_answer_var.get().strip().lower()

    if not question_text or not choice_alpha or not choice_bravo or not choice_charlie or not choice_delta or correct_answer not in ['a', 'b', 'c', 'd']:
        messagebox.showerror("Oops!", "Complete all the fields and use a, b, c or d for the correct answer.")
        return