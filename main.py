# building task
def load(filename):
    tasks=[]
    try:
        with open(filename,'r') as file:
            tasks=file.read().splitlines()
    except:
        print("error loading tasks")
    return tasks

def save_task(tasks):
    try:
        with open(filename,'w') as file:
            for task in tasks:
                file.write(f"{task}\n")
    except:
        print("error adding tasks")
    return 'your tasks are added successfully'


def addtask(tasks):
    task=str(input('enter a task: '))
    tasks.append(task)


def viewtask(tasks):
    if not tasks:
        print("no task has been created yet ")
    else:
        for task in tasks:
            print(task)

def deletetask(tasks):
    viewtask(tasks)
    task_no=int(input("please enter the task number you want to delete: "))
    if(task_no<len(tasks)):
        tasks.pop(task_no-1)
        print("task deleted")
    else:
        print("please enter a valid number: ")

def main():
    filename="Tasks.txt"
    tasks=load(filename)
    while True:
        print('Yout To-do list Menu')
        print('1:Add task')
        print('2:view task')
        print('3:Delete task')
        print('4:exit')
        choice=int(input("Please enter a number of your choice: "))
        if(choice==1):
            addtask(tasks)
        if(choice==2):
            viewtask(tasks)
        if(choice==3):
            deletetask(tasks)
        if(choice==4):
            save_task(tasks)
            print('Goodbye,see you soon!')
            return False


        

if(__name__=="__main__"):
    main()