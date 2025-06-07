class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

gorge = Person('Gorge', 20)
gorge.greet()

alice = Person('Alice', 40)
alice.greet()