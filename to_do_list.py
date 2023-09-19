tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")
    
def list_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}.{task}")

def mark_task_done(task_number):
    try:
        index = int(task_number)-1
        if 0 <= index<len(tasks):
            tasks[index] = f"[Done] {tasks[index]}"
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Quit")

    choice = input("Enter your choice:" )

    if choice =="1":
        task = input("Enter the task:" )
        add_task(task)
    elif choice =="2":
        list_tasks()
    elif choice =="3":
        task_number = input("Enter the task number to mark as done:" )
        mark_task_done(task_number)
    elif choice =="4":
        break
    else:
        print("Invalid choice. Please try again.")