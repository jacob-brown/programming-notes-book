# Python

## Basics

### Lists
Methods: 

* `append()`
* `clear()`
* `copy()`
* `count()`
* `extend()`
* `index()`
* `insert()`
* `pop()`
* `remove()`
* `reverse()`
* `sort()`


demoList = ["apple", "banana", "orange", "kiwi"]
print(demoList)

Adding/Removing items

demoList.append('cherry')
print(demoList) 

demoList.insert(1, 'grape')
print(demoList) 

join 2 lists

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

or...

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist + tropical

Removing items

demoList = ["apple", "banana", "orange", "kiwi"]

demoList.remove('apple')
print(demoList)

demoList.pop(1)
print(demoList)

del demoList[0]
print(demoList)

demoList.clear() # removes all items
print(demoList)

### Copying a list
make sure the lists aren't linked, with a deep copy

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

del thislist[1]
print(thislist)
print(mylist)

### Tuples

unchangeable

`count()` and `index()`


tupExample = (1, 2, 3)
tupExample

### Sets
unordered and unindexed, adding/removing is possible but not changing




thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 

### Dictionaries

fruitDict = {
    "type" : "apple",
    "colour" : ["red", "green"],
    "weight" : 200
}

print(fruitDict)

print(fruitDict["type"])




fruitDict.get("weight")

fruitDict.keys()

fruitDict.values()

fruitDict.items()

Changing, adding, and removing items in a dictionary

fruitDict = {
    "type" : "apple",
    "colour" : ["red", "green"],
    "weight" : 200
}

fruitDict["weight"] = 500
print(fruitDict)

fruitDict.update({"smell" : "appley"})
print(fruitDict)

fruitDict["season"] = "summer"
print(fruitDict["season"])

del fruitDict["colour"]
print(fruitDict)

### Loops


for i in range(0,5):
    print(i)

x = 0
while x < 6:
    print(x)
    x = x + 1
    

breaks within loops

x = 0
while x < 6:
    print(x)
    
    if x == 4:
        break
    
    x = x + 1

continue jumps back to the start of the loop

x = 0
while x < 6:
    x += 1
    if x == 4:
        continue
    print(x)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

### Conditions (If..Else)

a = 2
b = 20

if a > b:
    print("a is larger")
elif a == b:
    print("they are equal")
else:
    print("b is larger")
    


a = 200
b = 33
c = 500

if a > b or a > c:
  print("At least one of the conditions is True")

use `pass` to avoid an error.

if 1 > 10:
    pass

### List Comprehension

newList = ["apple", "banana", "cherry"]

[x for x in newList]

[x for x in newList if x != 'apple']

[x for x in newList if x != 'apple']

[x.upper() for x in newList]

### Functions and lambda

lambda can have only one expression

def printHello():
    print("Hello")

printHello()

addTen = lambda x : x  + 10

addTen(2)

x = lambda a, b : a * b
print(x(5, 6)) 

## Classes/Objects
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


## Modules
Code library or a local `.py` file

import numpy as np

np.array([1, 2, 3])

from pandas import DataFrame as df

df([1,2,3])

## RegEx
`import re`

`re.` methods:

* `findall` - Returns a list containing all matches
* `search` - Returns a Match object if there is a match anywhere in the string
    * `.span()` - returns a tuple containing the start and end positions of the match.
    * `.string` - returns the string passed into the function
    * `.group()` - returns the part of the string where there was a match
* `split` - Returns a list where the string has been split at each match
* `sub` - Replaces one or many matches with a string

*from w3*


## File Handling

`open(filename, mode)`

Mode types:

`"r"` - read

`"a"` - append

`"w"` - write

`"x"` - create

open, readlines,and close

```python
f = open("demofile.txt", "r")
print(f.readline())
f.close() 
```



https://www.w3schools.com/python/numpy_intro.asp

