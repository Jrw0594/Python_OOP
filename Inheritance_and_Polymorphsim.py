
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')
    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print('I am eating')
    
myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()
print('---------------')

#this will inherit the animal class
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def bark(self):
        print('woof')
    
mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()

print('-------------')

#polymophsim 


class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self): 
        return self.name + ' says woof'
    
class Cat():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' says meow!'
    
niko = Dog('niko')
felix = Cat('felix')
    
print(niko.speak())
print(felix.speak())

print('----------')

for pet in [niko,felix]:
    print(pet.speak())
    print('----------')
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(niko)
pet_speak(felix)
print('--------')

class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')
    
class Dog(Animal):
    
    def speak(self):
        return self.name + ' says woof!'
    
class Cat(Animal):
    def speak(self):
        return self.name + ' says meow!'
    
fido = Dog('fido')
isis = Cat('isis')

print(fido.speak())
print(isis.speak())


        