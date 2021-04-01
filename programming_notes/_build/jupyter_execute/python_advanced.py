# Python: Advanced

## Classes

**Classes** are like blueprints for creating objects.

**Instances** are what is built using the class.

The `__init__()` function is found in all **classes**. It is used to assign values to object properties, or  other operations when the *object is being created*.

`self` is used to reference the current instance of the class, and is used to access variables that belong to the class. *it doesn't need to be named self*

Classes can contain **methods** (in object functions)


class car:
    def __init__(self, make, topspeed):
        self.make = make
        self.topspeed = topspeed

blueCar = car("Ford", "150")

print(blueCar.make)
print(blueCar.topspeed)

add a method to the class

class animal:
    def __init__(self, name, weight, habitat):
        self.name = name
        self.weight = weight
        self.habitat = habitat
    
    def sayHello(self):
        print("Hello I am a " + self.name)

        
tiger =  animal("tiger", 200, "forest")

tiger.sayHello()

modifying object parameters is similar to normal python sytax  

tiger.weight = 220
print(tiger.weight)

del tiger.habitat
print(tiger.__dict__) # quick investigation

### Attribute Visibility

public - **no change**

protected - **1 underscore prefix**

private - **2 underscore prefix**

class employee:
    def __init__(self, name, salary, bonus):
        self.name = name # public
        self._salary = salary # protected
        self.__bonus = bonus # private
        
jacob = employee("jacob", 30000, 2000)
print(jacob.name)
print(jacob._salary)
#print(jacob.__bonus) # would return an error

### Inheritance
Inheritance allows us to define a class that inherits methods and properties from another class. 

**parent** and **child** classes will be used.



# Parent class

class animal:
    def __init__(self, name, weight, habitat):
        self.name = name
        self.weight = weight
        self.habitat = habitat
    
    def sayHello(self):
        print("Hello I am a " + self.name)

        
# Child class

class fish(animal):
    pass # used for empty classes

shark = fish("Great White", "1000", "tropical ocean")

print(shark.name)



if we were to add the `__init__()` function, the child overrides that of the parents class.

To keep it, add a call to the parents `__init__()` directly or use `super()`

class animal:
    def __init__(self, name, weight, habitat):
        self.name = name
        self.weight = weight
        self.habitat = habitat


# explicitly calling
class bird(animal):
    def __init__(self, name, weight, habitat):
        animal.__init__(self, name, weight, habitat)

        
# using super()
class mammal(animal):
    def __init__(self, name, weight, habitat):
        super().__init__(name, weight, habitat)

        
        
eagle = bird("Golden", 2, "mountains")
print(eagle.__dict__)

bear = mammal("Grizzly", 500, "forest")
print(bear.__dict__)

properties can also be added at the inheritance stage

class animal:
    def __init__(self, name, weight, habitat):
        self.name = name
        self.weight = weight
        self.habitat = habitat

        
class insect(animal):
    def __init__(self, name, weight, habitat, colonySize):
        super().__init__(name, weight, habitat)
        self.colonySize = colonySize
        self.exoskeleton = True # you can also add properties that aren't assigned
    
    def printColonySize(self):
        print("The ", self.name, " has a colony size of ", self.colonySize)

        
        
ant = insect("fire ant", 0.001, "tropical forest", 100000)

ant.printColonySize()

ant.__dict__

### Super - Extended

from - https://realpython.com/python-super/#what-can-super-do-for-you

`super(Square, self).__init__()`
the first element should be the same name as the **new class**

calling methods using super: `super().area()`

imagine that we don't want to inherite a method eg. a cube should not be able to use `area()` outside of the class. 

In this instance we should **modify** the method by using the same name



# superclass - parent
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# subclass - child
class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


class Cube(Square):
    # modify an existing method
    def area(self):
        face_area = super().area()  # using the area() method
        return face_area * 6

    # add a new method
    def volume(self):
        face_area = super().area()
        return face_area * self.length


print("square")
squareObj = Square(4)
print(squareObj.area())

print("cube")
cubeObj = Cube(4)
print(cubeObj.area())

### Multiple inheritance

We must be careful when inheriting from multiple classes.

For example, the below *will return an error*


**Method Resolution Order** - is the order in which the methods are called. 

`__mro__` - provides info on the order

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# inherit from 2 classes
class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area
        perimeter = super().perimeter
        return 0.5 * perimeter * self.slant_height + base_area

pyramid = RightPyramid(2, 4)
# pyramid.area() # returns an error

# method resolution order
RightPyramid.__mro__

note how the order is RightPyramid, Triangle, Square

We want to switch the order of Triangle and Square

class RightPyramidAlt(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area
        perimeter = super().perimeter
        return 0.5 * perimeter * self.slant_height + base_area

RightPyramidAlt.__mro__

There are still some issues though: 
1. two separate classes with the same method name and signature i.e. we are inheriting the `area()` method from Square and Triange
2. the new class doesn't distinguish between Triange and Square objects very well. i.e. they don't reference their superclass

Issue 1 resolution: name the method `area()` differently eg. `squ_area` and `tri_area`


Issue 2 resolution: 
* add `super().__init__()` to the `.__init__()` in Rectange and Trainge
* allow `.__init__()` to take keyword dictionary

Alternatively, we could define a new class 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# the new volume superclass
class Volume:
    def volume(self):
        return self.area() * self.height


# subclass
class Cube(Volume, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length


cube = Cube(2)
print(cube.volume())

### Iterators
Is an object that can be iterated upon. 

Specifically consitsting of the metods `__iter__()` and `__next__()`

`__iter__()` - returns the iterator object

`__next__()` - returns the next item in the sequence



class numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = numbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))



to stop the iteration use `StopIteration`

class numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = numbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

## Class Concepts

classes have a number of key concepts
* inheritance - creating a new class from a parent
* encapsulation - being unable to effect the core data, unless a function specifices this 
* Polymorphism - to use a common interface for multiple forms

### Inheritance

# Parent class
class animal:
    def __init__(self, species, habitat, size):
        self.species = species
        self.habitat = habitat
        self.size = size

    def __str__(self):
        return "I am a " + self.species

    def sayHelloSpecies(self):
        print("hello I am a " + self.species)

# child class
class fish(animal):
    def __init__(self, species, habitat, size):
        super().__init__(species, habitat, size)

    def fishSpeak(self):
        print("bubble bubble bubble")
        
        
        
        
skate = fish("skate", "north sea", 4)
skate.sayHelloSpecies()
skate.fishSpeak()
print(skate)

### Encapsulation 

note how the `__maxprice` cannot be changed without the use of the specificed function as it is a *private attribute*

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("selling at price {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()

c.sell()

# change the price - doesn't work! good
c.__maxprice = 9
c.sell()

# using setter function - works
c.setMaxPrice(1000)
c.sell()

### Polymorphism

We can have multiple common classes, that can be used by other functions/class/etc.

the `flying_test()` function uses the `fly()` method in both the parrot and emu classes. 

# parent
class animal:
    def __init__(self, species, habitat, size):
        self.species = species
        self.habitat = habitat
        self.size = size


class parrot(animal):
    def __init__(self, species, habitat, size):
        super().__init__(species, habitat, size)

    def fly(self):
        print("can fly")


class emu(animal):
    def __init__(self, species, habitat, size):
        super().__init__(species, habitat, size)

    def fly(self):
        print("cannot fly")


# define a common test
def flying_test(birdSpecies):
    birdSpecies.fly()


# create object and run tests
polly = parrot("parrot", "tropics", 1)
paul = emu("emu", "tropics", 67)
flying_test(polly)
flying_test(paul)


## Custom iterators
uses `__iter__()` and `__next__()` methods

`__iter__()` - returns the iterator object

`__next__()` - returns the next item in the sequence
    it also requires use of `StopIteration`


class powerTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


for i in powerTwo(3):
    print(i)





## Generators
Are a simple way of creating iterations

`yield` is used at least once in a function. It has the same effect as the `return` function, but pauses the functions state, allowing it to be iterable.

`__iter__()` and `__next__()` methods are automatically initiated

They are:
* memory efficient
* easier to understand


def powerTwoAlt(max = 0):
    n = 0 
    while n <= max:
        yield 2 ** n
        n += 1

for i in powerTwoAlt(3):
    print(i)

An alternative is in the style of a list comprehension, but uses `()` over `[]`

# list comprehension
listPowerTwo = [2 ** x for x in range(0, 4)]

# generator
generatorPowerTwo = (2 ** x for x in range(0, 4))

print(listPowerTwo)
print(generatorPowerTwo)

for i in generatorPowerTwo:
    print(i)

## Closure
if a function has a *nested* function with a value that must be *referenced in the enclosed function* then closure should be used. 

It is the concept of returning the nested function


def makePrinter(msg):
    
    def printer():
        print(msg)
        
    def doSomethingElse():
        return 0
    
    return printer

testPrint = makePrinter("hello there")
testPrint()

## Decorators
adds functionallity to existing code - *metacoding* 

decorators act as a wrapper

Divider example, we are aiming to add functionality to: 

```python
def divide(a, b):
    return a / b
```

# the decorator function
def describeDivide(func):
    def innerDivide(a, b):
        print("I am going to divide ", a, " and ", b)
    
        return func(a, b) # returns answer
    return innerDivide # returns statement


@describeDivide
def divide(a, b):
    return a / b


divide(10, 2)


Decorators can be **chained together**, making the code more modular  

in the below example:

`args` is the tuple of positional arguments

`kwargs` is the dictionary of keyword arguments

thus...

`function(*args, **kwargs)` is th ultimate python wildcard

**pseudocode for decorators** 
1. define function
2. define inner function allowing everything to pass
3. print `*`s / `%`s
4. Let the function run
5. print `*`s / `%`s
6. exit



def addStars(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def addPercentage(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


# now chain them 
@addStars
@addPercentage
def printBanner(msg):
    print(msg)

printBanner("Hello I am a banner")


## Getters, setters, and `property`

When using getters and setters it is important to ensure we have backwards compatibility. 

For example, assume we want to convert the below use getters and setters

class animal:
    def __init__(self, species):
        self.species = species

bear = animal("panda")

print(bear.species)

class animal:
    def __init__(self, species):
        self.setSpecies(species)
    
    def setSpecies(self, valueSpecies):
        self.__species = valueSpecies # note the attribute is private
    
    def getSpecies(self):
        return self.__species

bear = animal("panda")
print(bear.getSpecies())
bear.setSpecies("grizzly")
print(bear.getSpecies())

So one issue we now face is that `bear.species` has now been replaced with `bear.getSpecies()`

This is not backwards compatible...

This is where `property` comes in! 

`property(fget=None, fset=None, fdel=None, doc=None)`

`fget` - get value attribute

`fset` - set value attribute

`fdel` - delete value attribute

`doc` - string value


class animal:
    def __init__(self, species):
        self.setSpecies(species)
    
    def setSpecies(self, valueSpecies):
        self.__species = valueSpecies # note the attribute is private
    
    def getSpecies(self):
        return self.__species
    
    # enable backwards compatibility
    species = property(fget=getSpecies, fset=setSpecies)

bear = animal("panda")
print(bear.species)
bear.species = "grizzly"
print(bear.species)


### `@property` 

A more pythonic way, is to use the `@property`  decorator.

Which has:
* `getter (fget)` - this is the default with @property
* `setter (fset)`
* `deleter (fdel)`
* `mro`

When using the same name eg. `species` it is important that the visability is **private** or **protected** 

N.B. how `@property` is used for establising and getting and `@funcName.setter`/`@funcName.deleter` are used.

class animal:
    def __init__(self, species):
        self.species = species 
        
    @property 
    def species(self):
        return self.__species
    
    @species.setter
    def species(self, newSpecies):
        self.__species = newSpecies
        
    @species.deleter
    def species(self):
        del self.__species

# initiate and get
pandaBear = animal("panda")
print(pandaBear.species)

# set
pandaBear.species = "grizzly"
print(pandaBear.species)

# delete
print(pandaBear.__dict__)
del pandaBear.species
print(pandaBear.__dict__)

## Instant, Class, and Static Methods

**Instant** - a basic class method, takes `self` and points to an instance of the class

**Class** - takes a class parameter `cls` and points to the class when the method is called

**Static** - do not require a class instance creation, thus are not dependent on the state of the object.

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
obj.method()

obj.classmethod()

obj.staticmethod()

### Class methods: when to use

One example of usage is with *factory functions*. These are predefined methods that feed back into the class.

**Pizza example.**

Assume we have a class `pizza` that allows users to define toppings. We also want to have some preset pizza types however. 


class pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self): 
        return "Ingredients: {}".format(self.ingredients)
    
    @classmethod
    def jacobSpecial(cls):
        return cls(['mozzarella', 'pineapple', 'sweetcorn', 'olives'])
    
    
# we can use the class as normal
standardPizza = pizza(['mozzarella'])
print(standardPizza)


# or we can call the classmethod
print(pizza.jacobSpecial())


# note how it exists in the new object
print(standardPizza.jacobSpecial()) 

### Static methods: when to use

Day to day, static methods aren't used often.

A large benefit is improving **code readability**, signifying that the method does not depend on state of the object itself.

When then?:
1. grouping a utility function in a class (because it can't go anywhere else)
2. having a single implementation



# 1. grouping a utility function in a class (because it can't go anywhere else)

class Dates:
    def __init__(self, date):
        self.__date = date
    
    def getDate(self):
        return self.__date
    
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

dateObj = Dates("01/01/2020")
print(dateObj.getDate())

Dates.toDashDate("01/01/2020")

`toDashDate` is completely independent of the class and object, but storing the method here makes sense.

# 2. having a single implementation

class Dates:
    def __init__(self, date):
        self.date = date
    
    def getDate(self):
        return self.date
    
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")
    

class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)    

dateObj = Dates("01/01/2020")
print(dateObj.getDate())


dateFromDB = DatesWithSlashes("15/12/2016")
print(dateFromDB.getDate())

here we wouldn't want `DatesWithSlashes` to override the static utility 

## Magic Methods

## 

`__repr__()` is used to help with printing the object. 

it gets called when you try to convert an object into a string through the various means that are available eg. `print()`, `str()`, etc.

## Initiate and call method
sometimes you may want to call a method when the class is initiated

class animal:
    def __init__(self, name):
        self.name = name
        self.sayName() # initiate here

    def sayName(self):
        print("I am a", self.name)

dog = animal("dog")

## kwargs
Usage of `**kwargs` with classes. 
Allow the user to input as many fields as they wish. 


class Employee:
    def __init__(self, fullname, **kwargs):
        fullname_array = fullname.split()
        self.name = fullname_array[0]
        self.lastname = fullname_array[1]
        self.__dict__.update(kwargs)


jacob = Employee("Jacob Brown", height=180, mobile = "0123456789")
print(jacob.name)
print(jacob.lastname)
print(jacob.height)
print(jacob.__dict__)