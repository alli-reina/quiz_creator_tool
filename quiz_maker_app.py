import tkinter as tk
from tkinter import messagebox

def save_question():
    question_text = entry_question.get().strip()
    choice_alpha = entry_alpha.get().strip()
    choice_bravo = entry_bravo.get().strip()
    choice_charlie = entry_charlie.get().strip()
    choice_delta = entry_delta.get().strip()
    correct_answer = correct_answer_var.get().strip().lower()
    