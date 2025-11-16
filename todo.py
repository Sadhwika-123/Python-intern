TASK_FILE = "tasks.txt"     # <-- MUST BE AT THE TOP

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n=== TO-DO LIST APPLICATION ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            print("\n--- Your Tasks ---")
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added successfully!")
            else:
                print("Task cannot be empty!")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove!")
                continue

            print("\n--- Remove Task ---")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                index = int(input("Enter task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Enter a valid number!")

        elif choice == "4":
            print("Exiting... Tasks saved.")
            save_tasks(tasks)
            break

        else:
            print("Invalid choice! Enter 1-4.")

if __name__ == "__main__":
    main()
