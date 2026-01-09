def get_todos(filepath):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        todos = get_todos(filepath="todos.txt")

        todos.append(todo)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action or 'display' in user_action:
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos, start=1):
            print(f"{index}. {item.strip()}")

    elif 'edit' in user_action:
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        try:
            number = int(input("Enter the number of todo you want to change: "))
            if 0 < number <= len(todos):
                todos[number - 1] = input("Enter the new todo: ").strip() + "\n"

                with open("files/todos.txt", "w") as file:
                    file.writelines(todos)
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Please enter a valid number.")

    elif 'complete' in user_action:
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        try:
            number = int(input("Enter the todo number to mark complete: "))
            if 0 < number <= len(todos):
                removed = todos.pop(number - 1)

                with open("files/todos.txt", "w") as file:
                    file.writelines(todos)

                print(f"Completed: {removed.strip()}")
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Please enter a valid number.")

    elif 'exit' in user_action:
        break

    else:
        print("Wrong Function used!")

print("Bye!!")
