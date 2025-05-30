name = input('Enter your name: ')
if len(name) < 3 :
    print('Name must be at least 3 characters long')
elif len(name) > 10 :
    print('Name must be less than 10 characters long')
else :
    print('Name looks good!!')
