# ✅ Todo List Management System

A beginner-friendly Python Todo List project built using **Object-Oriented Programming (OOP)**.

This project allows users to:

- ✅ Add Tasks
- ✅ Show Tasks
- ✅ Remove Tasks
- ✅ Exit Program

This project is perfect for Python beginners to practice:

- Classes & Objects
- Lists
- Methods
- Loops
- Conditional Statements
- User Input Handling

---

# 📌 Features

- Add new tasks
- Display all tasks
- Remove completed tasks
- Simple menu-driven system
- Beginner-friendly code structure

---

# ▶️ How To Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

## 2️⃣ Open Project Folder

```bash
cd your-repository-name
```

## 3️⃣ Run Program

```bash
python main.py
```

---

# 💻 Project Code

```python
class Todo:

    def __init__(self):
        print("Welcome todo app.")

    tasks = []

    def add_task(self, task):
        self.task = task
        self.tasks.append(self.task)

    def show_tasks(self):
        print(self.tasks)

    def remove_task(self, task):
        self.task = task
        self.tasks.remove(self.task)


c1 = Todo()

while True:

    choice = input(
        "Please select one option...\n"
        "1. Add task\n"
        "2. Show tasks\n"
        "3. Remove task\n"
        "4. Exit\n"
        "Enter choice : "
    )

    if (choice == "1"):

        task = input("Enter task : ")
        c1.add_task(task)

    elif (choice == "2"):

        c1.show_tasks()

    elif (choice == "3"):

        task = input("Enter task : ")
        c1.remove_task(task)

    elif (choice == "4"):

        print("Exit")
        print("Thanks!!")
        break

    else:
        print("You entered an invalid option.")
        print("Please enter valid option.")
```

---

# 🧪 Example Output

```bash
Welcome todo app.

Please select one option...
1. Add task
2. Show tasks
3. Remove task
4. Exit
Enter choice : 1

Enter task : Learn Python

Please select one option...
1. Add task
2. Show tasks
3. Remove task
4. Exit
Enter choice : 2

['Learn Python']
```

---

# 📚 Concepts Used

| Concept | Description |
|---|---|
| Class | Creates Todo app blueprint |
| Object | Creates Todo app instance |
| List | Stores tasks |
| Methods | Performs task operations |
| while loop | Runs menu repeatedly |
| if-elif-else | Handles menu options |

---

# 🚀 Future Improvements

You can improve this project by adding:

- Task Completion Status
- Due Dates
- File Handling
- GUI using Tkinter
- Database Integration
- Priority Levels
- Search Tasks Feature
- Update Task Feature

---

# 👨‍💻 Author

**Wajid Ali**

Python Beginner Developer 🚀

---