tasks = []
status = {}

def divider():
    print("__________________________________________________________________________________")

def add_task():
    divider()
    new_task = input("Enter a new task: ").capitalize()
    if new_task in tasks:
        print("Task already exists...")
        return
    else:
        tasks.append(new_task)
        status.update({new_task: "incomplete"})
        view_task()

def remove_task():
    while True:
        divider()
        if not tasks:
            print("No available tasks...")
            break
        else:
            print("Which of these tasks would you like to remove?")
            print(tasks)
            remove_choice = input().capitalize()
            if remove_choice not in tasks:
                print("ERROR: Invalid Input")
                input("Press any key to try again...")
            else:
                status.pop(remove_choice)
                tasks.remove(remove_choice)
                view_task()
                break

def view_task():
    divider()
    if not tasks:
        print("No available tasks...")
        return
    else:
        for task in tasks:
            print(f"{task} : {status.get(task)}")

def mark_task():
    while True:
        divider()
        if not tasks:
            print("No available tasks...")
            break
        else:
            print("Which task have you completed?")
            print(tasks)
            marked_choice = input("Select a task: ")
            if marked_choice not in tasks:
                print("ERROR: Invalid Input")
                input("Press any key to try again...")
            else:
                status[marked_choice] = "complete"
                view_task()
                break

while True:
    divider()
    print("What would you like to do?")
    print()
    print("1. Add a Task")
    print("2. Remove a Task")
    print("3. View all Tasks")
    print("4. Mark a Task as complete")
    print("5. Exit")
    print()
    choice = input()
    if not choice.isnumeric():
        print("ERROR: Invalid Input")
        print("Please provide an integer(1-5)")
        input("Press any key to try again... ")
    else:
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            break
        else:
            print("ERROR: Invalid Input")
            input("Press any key to try again... ")