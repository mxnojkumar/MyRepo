from functions import get_todos, write_todos

while True:
    user_input = input("Type add, show, edit, complete or exit: ")
    user_input = user_input.strip()
    user_input = user_input.lower()
    
    # adding a new todo to the file
    if user_input.startswith('add'):
        todo = user_input[4:]
        
        todos = get_todos()
        
        todos.append(todo + '\n')
        
        write_todos(todos)
        
    # showing the existing todos in file    
    elif user_input.startswith('show'):
        
        todos = get_todos()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
            
    # editing an existing todo with another      
    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            print(number)
            
            number = number - 1
            
            todos= get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            write_todos(todos)
        
        except ValueError:
            print("Your command is not valid.") 
            continue
    
    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from todos"
            print(message)
            
            
        except IndexError:
            print("There is no item with that number.")
            continue
        
    elif user_input.startswith('exit'):
        break
    
    else:
        print("Command is not valid.")
        
print("Bye!")
    