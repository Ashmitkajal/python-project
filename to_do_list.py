todo_list = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        todo_list.append(task)
        print(f"✅ Task added: '{task}'")
    else:
        print("⚠️ Task cannot be empty!")

def view_tasks():
    if not todo_list:
        print("📭 No tasks in the list.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"🗑️ Task removed: '{removed}'")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Goodbye! Your tasks will not be saved after exit.")
            break
        else:
            print("⚠️ Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
