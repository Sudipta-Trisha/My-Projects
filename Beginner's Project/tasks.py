tasks = []


def add(task_list, task):
    task_list.append(task)
    print("Task added successfully!")


def view(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        print("My To-Do List: ")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")


def mark_completed(task_list, task_index):
    if 1 <= task_index <= len(task_list):
        completed_task = task_list.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed!")
    else:
        print("Invalid task index.")

