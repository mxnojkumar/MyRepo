todos = []

while True:
    user_option = input("Type add, show, or exit:")
    match user_option:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'exit':
            break
        