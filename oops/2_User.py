class User:
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.__password = password #private variable will have __ prefix
        self._email = email #protected variable will have _ prefix

    #java way to create getters and setters
    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = new_email

    # getters and setter python way
    @property
    def password(self):
        print("password was read!")
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password



user1 = User("john","andsdk", "*urijf$$3wj0")
print(f'Before updating email, the email is: {user1.get_email()}')
print(f'Before updating password, the password is: {user1.password}')


user1.set_email("john@gmail.com")
user1.password = "8u^ydgdj<>"
print(f'After updating email, the value is: {user1.get_email()}')
print(f'After updating password, the value is: {user1.password}')