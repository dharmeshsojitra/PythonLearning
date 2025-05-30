user_input = input('> ')

while user_input.lower() != 'exit':
    if user_input.lower() == 'help':
        print(">to start car, type 'start'")
        print(">to stop car, type 'stop'")
        print(">to exit the game, type 'exit'")
    elif user_input.lower() == 'start':
        print('car started')
    elif user_input.lower() == 'stop':
        print('car stopped')
    else:
        print('you entered wrong input')
        break
    user_input = input('>')
print('game exited')