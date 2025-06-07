class User:
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.__password = password #private variable will have __ prefix
        self._email = email #protected variable will have _ prefix

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = new_email


    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password



user1 = User("john","andsdk", "*urijf$$3wj0")
print(f'Before updating email, the email is: {user1.get_email()}')


user1.set_email("john@gmail.com")
print(f'After updating email, the value is: {user1.get_email()}')