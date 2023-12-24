from tasks import *


def display_menu():
    print("#######------------- TO-DO LIST ---------#########")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")


def main():
    tasks = []

    while True:
        display_menu()
        print("\n")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            add(tasks, task)
        elif choice == "2":
            view(tasks)
        elif choice == "3":
            view(tasks)
            task_index = int(input("Enter the index of the task to mark as completed (0 to cancel): "))

            if task_index != 0:
                mark_completed(tasks, task_index)

        elif choice == "4":
            print("Exiting the to-do list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


main()
