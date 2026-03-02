# task 1 Simple To-Do List Application

# Create an empty list to store tasks
tasks = []

# Infinite loop to keep program running
while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)   # Add task to list
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_num = int(input("Enter task number to delete: "))

            # Check if number is valid
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    # Exit Program
    elif choice == "4":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
