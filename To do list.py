#This project is still in progress.
while True:
    tasks=[]
    print("---------To do List--------------------")
    print("1.Add to list\n2.Remove from list\n3.Check your tasks.\n4.exit")
    choice=input()
    
    match choice:
        case 1:
            Add()
        case 2:
            delete()
        case 3:
            if not tasks:
                print("Your to do list is empty.")
            else    
                for i ,task in enumerate(tasks,1)
                print(f"{i}.{task})
        case 4:
            break
     
print(:"Exiting............................:)")

def Add(tasks):
    print("Enter the task you want to add.")
    in=input()
    tasks.append(in)
    

def delete():
    print("Choose the task you want to delete.")
     if not tasks:
                print("Your to do list is empty.")
            else    
                for i ,task in enumerate(tasks,1)
                print(f"{i}.{task})
   
