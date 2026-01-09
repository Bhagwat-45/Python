todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file_read = open('files/todos.txt','r')
            todos = file_read.readlines()
            file_read.close()
            todos.append(todo)
            file_write = open("files/todos.txt","w")
            file_write.writelines(todos)
            file_write.close()
        case 'show' | 'display':
            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()


            for index,items in enumerate(todos):
                items = items.strip("\n")
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
