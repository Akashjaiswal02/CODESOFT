#********* TO-DO LIST **********

def display_menu():
    print("\nTo Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for num, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not done"
            print(f"{num}. {task['task']} ({status})")

def mark_task_done(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number to delete: ")) - 1
    if 0 <= num < len(tasks):
        del tasks[num]
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()