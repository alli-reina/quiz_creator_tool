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
        file.write(f"Question: {question_text}\n")
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
    entry_alpha.delete(0, tk.END)
    entry_bravo.delete(0, tk.END)
    entry_charlie.delete(0, tk.END)
    entry_delta.delete(0, tk.END)
    correct_answer_var.set("")

def exit_app():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

# Title
root = tk.Tk()
root.title("Quiz Creator Tool")
root.geometry("400x500")
root.configure(bg="#ffe6f7")

# Header
tk.Label(root, text="✨Quiz Creator✨", font=("Comic Sans MS", 20, "bold"), bg="#ffe6f7", fg="#9933cc").pack(pady=10)
tk.Label(root, text="Enter your question below", font=("Helvetica", 12), bg="#ffe6f7", fg="#cc66ff").pack()

# Question Entry
entry_question = tk.Entry(root, width=50, bg="white", fg="#660066")
entry_question.pack(pady=8)

# Choices Entry
tk.Label(root, text="Choice A:", bg="#ffe6f7", fg="#cc66ff").pack()
entry_alpha = tk.Entry(root, width=40, bg="white", fg="#660066")
entry_alpha.pack(pady=2)

tk.Label(root, text="Choice B", bg="#ffe6f7", fg="#cc66ff").pack()
entry_bravo = tk.Entry(root, width=40, bg="white", fg="#660066")
entry_bravo.pack(pady=2)

tk.Label(root, text="Choice C:", bg="#ffe6f7", fg="#cc66ff").pack()
entry_charlie = tk.Entry(root, width=40, bg="white", fg="#660066")
entry_charlie.pack(pady=2)

tk.Label(root, text="Choice D:", bg="#ffe6f7", fg="#cc66ff").pack()
entry_delta = tk.Entry(root, width=40, bg="white", fg="#660066")
entry_delta.pack(pady=2)

# Correct Answer Entry
tk.Label(root, text="Correct Answer (a/b/c/d):", bg="#ffe6f7", fg="#cc66ff").pack(pady=10)
correct_answer_var = tk.StringVar()
tk.Entry(root, textvariable=correct_answer_var, width=10, bg="white", fg="#660066").pack()

# Buttons
tk.Button(root, text="💾Save Question", command=save_question, bg="#cc66ff", fg="white", font=("Arial", 11, "bold")).pack(pady=15)
tk.Button(root, text="❌Exit", command=exit_app, bg="#ff6699", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

root.mainloop()
