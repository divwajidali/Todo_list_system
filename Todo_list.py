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
    choice = input("Please select one option...\n1. Add task\n2. Show tasks\n3. Remove task\n4. Exit\nEnter choice :")

    if (choice == "1"):
        
        task = input("Enter task :")
        c1.add_task(task)

    elif (choice == "2"):
        c1.show_tasks()

    elif (choice == "3"):
        task = input("Enter task :")
        c1.remove_task(task)

    elif (choice == "4"):
        print("Exit\nThanks!!")
        break

    else:
        print("You entered an invalid option. Please entered valid option.")