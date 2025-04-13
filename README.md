# 📝 Quiz Creator (Terminal-Based)

A terminal-based Python application that allows you to easily create, manage, and store multiple-choice quiz questions — right from your command line!

---

## ✨ Features

- **Interactive**: Enter quiz questions and choices through the terminal.
- **Multiple Choice Support**: Each question supports 4 choices (A to D).
- **Answer Validation**: Ensures the correct answer is only 'a', 'b', 'c', or 'd'.
- **Auto-Save**: All questions and answers are saved to a `.txt` file.
- **Summary View**: Displays all added questions at the end of the session.
- **Organized Output**: All data is saved into a dedicated folder.

---

## 📁 Folder Structure

It is recommended to place the script inside a dedicated folder to keep your project and quiz data organized:

```
quiz_creator/
│
├── quiz_creator.py
├── quiz.txt
└── README.md
```

---

## ▶️ How to Run

1. **Clone this repository** or download the files:

```bash
git clone https://github.com/yourusername/quiz_creator.git
```

2. **Navigate to the project folder:**

```bash
cd quiz_creator
```

3. **Check if Python is installed:**

```bash
python --version
```

4. **Run the application:**

```bash
python quiz_creator.py
```

---

## 💬 Sample Output

```
Question: What is the capital of France?
Choice A: Berlin
Choice B: Paris
Choice C: Madrid
Choice D: Rome
Correct answer (a/b/c/d): b

```

---

## 📌 Notes

- You can edit or remove saved questions by modifying the `quiz.txt` file.
- The app automatically adds separators (`---`) between questions for better readability.
- Only 'a', 'b', 'c', or 'd' (lowercase) are accepted for the correct answer.

---

## 👩‍💻 Author

**Jonalyn Antoc**    
🔗 (https://github.com/alli-reina)
