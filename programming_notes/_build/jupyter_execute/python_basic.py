# Python: Basics

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