todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index,items in enumerate(todos):
                print(f"{index+1}.{items}")
        case 'edit':
            number = int(input("Enter the number of todo you wanna change: "))
            todos[number-1] = input("Enter the new todo: ")
        case 'complete':
            number = int(input("Enter the todo number to mark the todo complete: "))
            todos.pop(number-1)
            for index,items in enumerate(todos):
                print(f"{index}.{items}")
        case 'exit':
            break
        case whatever:
            print("You have entered the wrong choice!")

print("Bye!!")
