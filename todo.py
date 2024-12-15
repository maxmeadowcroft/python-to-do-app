"""
todo.py - Maximus Meadowcroft

This program is the main program for the code of this ToDo app.
In it the program will loop, asking you to either select a task to modify, or add a new task.

Still need to implement
- Adding tasks functionality
- Modifying tasks functionality
"""


def main():
    todoItems = {}  # Empty dictionary to store items

    menu = """
    ToDo List. Please enter an option:
    1. View tasks
    2. Exit
    """

    while True:  # infinite loop
        print(menu)
        user_input = input(">")
        if user_input == '1':
            pass
        elif user_input == '2':
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
