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
    
    with open("quiz.txt", "a", encoding="utf-8") as file:
        file.write(f"Question: {question}\n")
        file.write(f"Alpha) {choice_alpha}\n")
        file.write(f"Bravo) {choice_bravo}\n")
        file.write(f"Charlie) {choice_charlie}\n")
        file.write(f"Delta) {choice_delta}\n")
        file.write(f"Answer: {correct_answer}\n")
        file.write("---\n")
    
    messagebox.showinfo("Saved", "Your question is saved!")
    clear_fields()

def clear_fields():
    entry_question.delete(0, tk.END)
    entry_bravo.delete(0, tk.END)
    entry_bravo.delete(0, tk.END)
    entry_charlie.delete(0, tk.END)
    entry_delta.delete(0, tk.END)
    correct_answer_var.set("")

def exit_app():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()