class Animal:
    def walk(self):
        print("walking")


class Dog(Animal):
    def bark(self):
        print("barking")

class Cat(Animal):
    pass

dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()