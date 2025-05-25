# global variables
sentence = "TO- DO- LIST"
dash = "--------------------"
works = []
date = "" 

def heading():
    global date
    if not date:
        date = input('Enter date: ')
    print(sentence.center(160))
    print(dash.center(160))
    print(date.center(160))

def add():
    task = input('List those works dear😉: ')
    works.append(task)
    print("Task added!\n")

def save():
    with open('todo.txt', 'w') as file:
        file.write(sentence.center(160) + '\n')
        file.write(dash.center(160) + '\n')
        file.write(date.center(160) + '\n\n')
        for i, task in enumerate(works, start=1):
            file.write(f"{i}. {task}\n")
    print('\nSaved successfully!\n')

def load():
    print("\nTasks saved:")
    for i, task in enumerate(works, start=1):
        print(f"{i}. {task}")
    print()

def menu():
    while True:
        heading()
        print('\n1. Add tasks')
        print('2. Save tasks')
        print('3. Load tasks')
        print('4. Exit')

        try:
            choice = int(input("\nEnter choice from menu: "))
        except ValueError:
            print("Please enter a number 🙄!\n")
            continue

        if choice == 1:
            add()
        elif choice == 2:
            save()
        elif choice == 3:
            load()
        elif choice == 4:
            print("Bye 👋")
            break
        else:
            print("Choose a correct number 🙄!\n")

menu()
