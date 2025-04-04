class Person:
    def __init__(self,name):
        print('constructor :',self)
        self.name = name
    def talk(self):
        print('I am talking to',self.name)

print(Person('kevin').talk())