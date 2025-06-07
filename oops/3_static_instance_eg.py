class User:
    user_count = 0

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        User.user_count += 1


    def display_user(self):
        print(f'User name: {self.user_name}, password: {self.password}')
        print(f'total user count is: {User.user_count}')


john = User('John', '(oeirjf')

john.display_user()

john = User('John', '(oeirjf')
john.display_user()
