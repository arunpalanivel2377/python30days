"""
🎯 Goal:
Build a simple Command-Line Interface (CLI) app where users can:

Add tasks to a to-do list

View all tasks

Mark tasks as completed

Delete tasks
"""

tasks = []

print("=== Welcome to To-Do List App ===")

while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View unfinished tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        task = input("Enter your task: ")
        task = (task, False)
        tasks.append(task)
        print("Task added.")

    elif choice == 2:
        if not tasks:
            print("No tasks.")
        else:
            found = False
            print("\nUnfinished Tasks:")
            for i, (task, done) in enumerate(tasks):
                if not done:
                    print(f"{i + 1}. {task}")
                    found = True
            if not found:
                print("No unfinished tasks.")

    elif choice == 3:
        if not tasks:
            print("No tasks.")
        else:
            print("\nAll Tasks:")
            for i, (task, done) in enumerate(tasks):
                status = "✓" if done else "✗"
                print(f"{i + 1}. [{status}] {task}")
            try:
                index = int(input("Enter the index number to mark completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index] = (tasks[index][0], True)
                    print("Task marked as completed.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 4:
        if not tasks:
            print("No tasks.")
        else:
            print("\nAll Tasks:")
            for i, (task, done) in enumerate(tasks):
                status = "✓" if done else "✗"
                print(f"{i + 1}. [{status}] {task}")
            try:
                index = int(input("Enter the index number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Deleted task: {removed[0]}")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 5:
        print("Exiting! Goodbye 👋")
        break

    else:
        print("Invalid choice. Please select a number between 1–5.")
