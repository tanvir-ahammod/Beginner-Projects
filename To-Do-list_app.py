import json

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def show_menu():
    """Display menu options."""
    print("\n=== To-Do List App ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()