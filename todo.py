"""
todo.py - Maximus Meadowcroft

This program is the main program for the code of this ToDo app.
In it the program will loop, asking you to either select a task to modify, or add a new task.

Still need to implement
- Modifying tasks functionality
"""


def main():
    todoItems = {}  # Empty dictionary to store items

    menu = """
ToDo List. Please enter an option:    
1. View tasks    
2. Add tasks
3. Exit
"""

    while True:  # main loop
        print(menu)
        user_input = input("> ")
        # User chooses to view tasks
        if user_input == '1':
            count = 0
            keys = list(todoItems.keys())
            values = list(todoItems.values())
            for i in range(len(keys)):
                print(f"{i+1}. {keys[i]}\t{"(DONE)" if values[i] else ""}")
        # User chooses to add tasks
        elif user_input == '2':
            task_name = input("Please enter a task name\n> ")
            todoItems[task_name] = False
        # User chooses to exit
        elif user_input == '3':
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
