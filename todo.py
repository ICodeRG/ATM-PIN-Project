# Simple To-Do List App (Command-Line Version)

tasks = []  # List to store tasks

def show_tasks():
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    """Add a new task."""
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    """Remove a task."""
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def main():
    """Main loop to run the app."""
    while True:
        print("\nOptions: 1) Show Tasks  2) Add Task  3) Remove Task  4) Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
