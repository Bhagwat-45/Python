user_prompt = "Enter a todo: "
todos_list = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    if todo == "Exit":
        break
    todos_list.append(todo)

print(todos_list)

