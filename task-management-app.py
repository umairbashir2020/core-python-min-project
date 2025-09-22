def task():
    tasks = [] # task list
    print("---------Welcome to the task management app----------")

    total_task = int(input("Enter the number of today's task = "))

    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ") 
        tasks.append(task_name)

    print(f"Today's task are\n {tasks}")

    while True:
        operations =int(input(f"Select option \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        
        if operations == 1:
            add_task =input('Enter your task you want to add = ')
            tasks.append(add_task)
            print(f"Task {add_task} has been successfully added..")

        elif operations == 2:
            update_task = input("Enter task name you want to update = ")
            if update_task in tasks:
                update = input("Enter your new task = ")
                task_index = tasks.index(update_task) #2
                tasks[task_index] = update
                print(f"Your task {update} has been successfully updated..")

        elif operations == 3:
            delete_task = input("Enter your task name you want to delete = ")
            if delete_task in tasks:
                task_index = tasks.index(delete_task)
                del tasks[task_index]
                print(f"Task {delete_task} has been successfully deleted... ")
            
        elif operations == 4:
            view_task = tasks # display all task
            print(f"Total task = {view_task}")
        
        elif operations == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid Input...")

task() # call the function