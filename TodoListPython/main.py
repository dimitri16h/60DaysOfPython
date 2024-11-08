user_prompt = "Enter todo: "

todos = []

while todo != "":
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
