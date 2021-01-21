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

note how the `__maxprice` cannot be changed without the use of the specificed function.

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


