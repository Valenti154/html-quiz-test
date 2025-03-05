# [
#     {"task": "Buy milk", "done": False},
#     {"task": "Walk the dog", "done": False},
#     {"task": "Read a book", "done": False},
#     {"task": "Finish homework", "done": False},
#     {"task": "Call mom", "done": False}
# ]

# Task list (list of dictionaries)
tasks = []

def add_task():
    """Add a new task"""
    
    task_description = input("Enter task description: ")
    tasks.append({"task": task_description, "done": False})
    print(f'Task "{task_description}" added!\n')

def view_tasks():
    """Display task list"""
    if not tasks:
        print("The task list is empty.\n")
        return

    print("\n===== Task List =====")
    for i, task in enumerate(tasks, start=1):
        status = "[✔]" if task["done"] else "[ ]"
        print(f"{i}. {task['task']} {status}")
    print()

def mark_task_done():
    """Mark a task as completed"""
    view_tasks()
    try:
        num = int(input("Enter the number of the completed task: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print(f'Task "{tasks[num]["task"]}" marked as completed!\n')
        else:
            print("Error: Task number out of range!\n")
    except ValueError:
        print("Error: Please enter a valid number!\n")

def remove_task():
    """Remove a task"""
    view_tasks()
    try:
        num = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= num < len(tasks):
            removed_task = tasks.pop(num)
            print(f'Task "{removed_task["task"]}" removed!\n')
        else:
            print("Error: Task number out of range!\n")
    except ValueError:
        print("Error: Please enter a valid number!\n")

def main():
    """Main menu loop"""
    while True:
        print("\n===== Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Goodbye!")
            break  # Exit the program
        else:
            print("Error: Please choose an option from 1 to 5!\n")

if __name__ == "__main__":
    main()