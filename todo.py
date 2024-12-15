"""
todo.py - Maximus Meadowcroft

This is a simple To-Do list application in Python.
"""

def main():
    todo_items = {}  # Dictionary to store tasks and their completion status

    while True:
        # Display main menu
        print("""
ToDo List - Please choose an option:
1. View tasks
2. Add a task
3. Exit
""")
        user_input = input("> ").strip()

        # View tasks
        if user_input == '1':
            if not todo_items:
                print("No tasks available. Add some tasks first!")
                continue

            # Show tasks
            print("\nTasks:")
            for idx, (task, done) in enumerate(todo_items.items(), start=1):
                status = "(DONE)" if done else ""
                print(f"{idx}. {task} {status}")

            # Task modification options
            print("\nEnter the task number to modify it, or type 'm' to return to the main menu.")
            task_choice = input("> ").strip()

            if task_choice.lower() == 'm':
                continue
            elif task_choice.isdigit() and 1 <= int(task_choice) <= len(todo_items):
                task_index = int(task_choice) - 1
                task_name = list(todo_items.keys())[task_index]

                print(f"\nTask: {task_name}")
                print("1. Mark as Done")
                print("2. Delete Task")
                print("3. Return to Task List")
                action = input("> ").strip()

                if action == '1':  # Mark as Done
                    todo_items[task_name] = True
                    print(f"Task '{task_name}' marked as done.")
                elif action == '2':  # Delete Task
                    del todo_items[task_name]
                    print(f"Task '{task_name}' deleted.")
                elif action == '3':  # Return to Task List
                    continue
                else:
                    print("Invalid option. Returning to the main menu.")
            else:
                print("Invalid task selection. Returning to the main menu.")

        # Add a task
        elif user_input == '2':
            task_name = input("Enter the task description: ").strip()
            if task_name in todo_items:
                print("This task already exists.")
            else:
                todo_items[task_name] = False
                print(f"Task '{task_name}' added.")

        # Exit
        elif user_input == '3':
            print("Exiting the ToDo app. Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
