'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    age = 0

    object_name =""

    def __init__(self, age, object_name):
        self.age = age
        self.object_name = object_name
    
    def increase_age(self):
        self.age = self.age + 1
        print(self.age)

    def say_greeting(self):
        object_name = self.object_name
        print(f"Hello World! My name is {object_name}!")
    
    def count_to_age(self):
        for a in range(0,self.age):
            print(a)

x = Person(20, "Lonny")

x.increase_age()
x.say_greeting()
x.count_to_age()




# You won't need to call anything here.