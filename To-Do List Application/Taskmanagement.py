todo = []

while True:
    print("\n1.Add Task\n2.View Tasks\n3.Delete Task\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        todo.append(task)
        print("Task Added!")
    
    elif choice == 2:
        print("\nYour Tasks:")
        for i, t in enumerate(todo, 1):
            print(i, t)

    elif choice == 3:
        num = int(input("Enter task number to delete: "))
        if num <= len(todo):
            todo.pop(num-1)
            print("Task Deleted!")
        else:
            print("Invalid Number")

    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
