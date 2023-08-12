import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is", now)


while True:
    
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    
    # Check if user action is "add"
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):      
        todos = functions.get_todos()
        # new_todos = [item.strip('\b') for item in todos]
            
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"    
            print(row)
            
    elif user_action.startswith('edit'):
        
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1     
            todos = functions.get_todos()   
            new_todo = input("Enter new to-do: ")
            todos[number] = new_todo + '\n'
            
            functions.write_todos(todos)
                
        except ValueError:
            print('======================================')
            print("Your command is not valid.")
            print('======================================')
            continue

        
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos = functions.get_todos()
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            functions.write_todos(todos)
            
            message = f" To-do {todo_to_remove} was removed from the list."
            print('======================================')
            print(message)
            print('======================================')
            
        except IndexError:
            print("There is no item with that index number")
            continue
        
    elif user_action.startswith('exit'):
        break
        
    else:
        print('======================================')
        print('Command is not valid')
        print('======================================')
print("Bye")

