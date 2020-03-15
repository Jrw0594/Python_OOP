class Dog():
    
    #class object attribute
    #Same for any instance of a class
    species = 'mammal'
    
    #init is a constructor of a class
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        #boolean for spots
        self.spots = spots

#Operations/Actions ---> Methods
    def bark(self,age):
        return('Woof! My name is {} and i am {} years old'.format(self.name,age))
    
my_dog = Dog('Shiz Tzu','Sammy',False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark(7))

class Circle():
    
    #Class object attribute
    pi = 3.14
    
    def __init__(self,radius=1):
        
        self.radius = radius
        #can use name of class instead of self
        self.area = radius*radius*Circle.pi
    
    #Method
    def get_circumference(self):
        return self.radius * self.pi * 2
my_circle = Circle(30)
print('---------------------')
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())
