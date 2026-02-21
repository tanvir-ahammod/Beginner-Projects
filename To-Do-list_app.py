tasks=[]

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice=input("Choose an option (1-4): ")

    if choice=="1":
        task=input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice=="2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

    elif choice=="3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            try:
                task_num=int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task=tasks.pop(task_num-1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice=="4":
        print("Exiting the To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 4.")

