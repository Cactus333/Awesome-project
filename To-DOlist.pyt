# Function to display the menu
def display_menu():
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")


# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")


# Function to remove a task
def remove_task(tasks):
    print("Current tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    choice = int(input("Enter the number of the task to remove: "))
    if 1 <= choice <= len(tasks):
        removed_task = tasks.pop(choice - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid choice!")


# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")


def main():
    tasks = []  # List to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
