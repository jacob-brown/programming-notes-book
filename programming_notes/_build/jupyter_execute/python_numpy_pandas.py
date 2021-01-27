# Python: Numpy and Pandas

## Numpy

import numpy as np

arr  = np.array([1, 2, 3, 4, 5])

print(arr)

check the number of dimensions


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

c = np.array([[1, 2, 3], [4, 5, 6]])
print(c.shape)

### Adding arrays (vectorisation)

N.B. this doesn't concatenate the arrays

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 4])

arr1 + arr2

### Slicing



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr[0:3])
print(arr[3:]) 
print(arr[0:8:2]) # with a step


2-D arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) # 2nd element 1:4

### Numpy Data Types
check with `.dtypes`


import numpy as np

arrString = np.array(['apple', 'banana', 'cherry'])
arrInt = np.array([1, 2, 3, 4])

print(arrString.dtype) 
print(arrInt.dtype)

create an array with a defined data type

arrString = np.array([1, 2, 3, 4], dtype='S') 
arrInt = np.array([1, 2, 3, 4], dtype='i')

print(arrString)
print(arrInt)

and we can convert the array

arr = np.array([1, 2, 3, 4], dtype="i")
print(arr.dtype)

newarr = arr.astype(float)
print(newarr.dtype)


### Copy and view

copy creates its own copy

view is linked to the original

`base` checks if array owns it's own data (`None` if true)

arrC = np.array([1, 2, 3, 4, 5])
arrV = np.array([1, 2, 3, 4, 5])

arrCopy = arrC.copy()
arrView = arrV.view()

arrC[0] = 9
arrV[0] = 9


print(arrC)
print(arrCopy)
print(arrV)
print(arrView)

print(arrCopy.base)
print(arrView.base)

### Reshape


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr.reshape(4, 3))
print("\n")
print(arr.reshape(2, 3, 2))
print("\n")
print(arr.reshape(2, -1)) # unknown dimension with -1


# flatten array
newArr = np.array([[1, 2, 3], [4, 5, 6]])
print(newArr.reshape(-1))


### Iterating

Arrays are iterable, if nested we can use `nditer`

`ndenumerate` can be used to note where in the array structure the element is located

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)
    
print("\n")    
# compared to
for x in arr:
    print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x) 

### Joining arrays

we can also specifcy joining on **rows** (`axis=0`) or **columns** (`axis=1`).




arr = np.array([1, 2, 3])

combo = np.concatenate((arr, arr))

print(combo)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

combo0 = np.concatenate((arr1, arr2), axis=0)
combo1 = np.concatenate((arr1, arr2), axis=1)

print(combo0)
print("\n")
print(combo1)

Similarly we can use `stack`, `hstack`, `vstack`, and `dstack`

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arrStack = np.stack((arr1, arr2), axis = 1)
arrHstack = np.hstack((arr1, arr2))
arrVstack = np.vstack((arr1, arr2))
arrDstack = np.dstack((arr1, arr2))

print("stack")
print(arrStack)
print("\nhstack")
print(arrHstack)
print("\nvstack")
print(arrVstack)
print("\ndstack")
print(arrDstack)


### Splitting arrays

`np.array_split` allows for non-exact splits, wereas `np.split` requires an exact match

splits can be carried out on multi-dimensional arrays with the axis specified.


arr = np.array([1, 2, 3, 4, 5, 6])

# split into 3 

arrSplit = np.array_split(arr, 3)
print(arrSplit)

# split into a non-multiple
arrSplitAlt = np.array_split(arr, 4)
print(arrSplitAlt)

as above we also have `hsplit`, `vsplit`, and `dsplit`

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

np.hsplit(arr, 3)

### Searching Arrays

arr = np.array(["red", "blue", "blue", "blue", "green", "green"])
print(np.where(arr == "green"))

**Binary Search**

`searchsorted` searches where the value should be inserted

arrays can also be used in this function

# binary 
arr = np.array([1, 5, 6, 8, 10])

print(np.searchsorted(arr, 2)) 


print(np.searchsorted(arr, 5)) # left most index given as default
print(np.searchsorted(arr, 5, side="right")) # right most index given


print(np.searchsorted(arr, [2, 3, 4]))


### Sorting


arrInt = np.array([3, 2, 0, 1])
print(np.sort(arrInt))

arrCol = np.array(["red", "blue", "blue", "blue", "green", "green"])
print(np.sort(arrCol))

# 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) 

### Filtering

arr = np.array([1, 2, 3, 4, 5, 6])

# general principle
newArr = arr[[True, True, False, True, False, False]]

print(newArr)

# better method
conditionArr = arr > 3
print(arr[conditionArr])

# the above for base lists would be
[i for i in arr if i > 3]

*Compare the speed of the two filtering methods*

**numpy** is far quicker


import time
import numpy as np


np.random.seed(0)
arr = np.random.randint(100, size=(1000))
repeats = 1000

def npFilter(x):
    for i in range(0,repeats):
        x[x >= 50]
    return 0

def baseFilter(x):
    for i in range(0,repeats):
        [i for i in x if i >= 50]
    return 0



start = time.time()
npFilter(arr)
print("numpy takes %f s to run." % (time.time() - start))

start = time.time()
baseFilter(arr)
print("base takes %f s to run." % (time.time() - start))


### Random numbers


from numpy import random

print(random.rand()) # range 0 and 1
print(random.randint(100)) # range 0 and 100
print(random.randint(100, size=(5)))

# choices
print("\nchoices")
print(random.choice([3, 5, 7, 9]))
print(random.choice([3, 5, 7, 9], size=2))
print(random.choice([3, 5, 7, 9], size=(2,5)))





## ufuncs

universal functions operate on `ndarray` objects

Good for:
* vectorisation
* broadcasting


x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

a = np.add(x, y)
print(a)


# is equivelent to
aa = np.array(x) + np.array(y) 
print(aa)

**Simple arithmetic**

`add()`

`subtract()`

`multiply()`

`divide()`

`power()`

`mod()` or `remainder()` - returns the remained

`divmod()` - returns the quotient and the mod in 2 arrays

`absolute()` or `abs()` - absolute values



**Rounding**

`fix()` and `trunc()` - Remove the decimals, and return the float number closest to zero

`around(in, no. of decimals)` - define the number of decimal places

`floor()` - nearest lowest integer

`ceiling()` - nearest highest integer


**Summation**

N.B. products (multiplication) can done in the same way with `prod()` and `cumprod()`

arr = np.array([1, 2, 3])

sum1 = np.sum([arr, arr])
print(sum1)

# sum of each array
sum2 = np.sum([arr, arr], axis = 1)
print(sum2)

# vertical sum
sum3 = np.sum([arr, arr], axis = 0)
print(sum3)

# cumulative sum [1, 2, 3] = [1, 1+2, 1+2+3]
sum4 = np.cumsum(arr)
print(sum4)


**Differences**


arr = np.array([10, 15, 25, 5])

diff1 = np.diff(arr) # equivelent to [10-15, 25-15, 5-25]
print(diff1)

# n is the number of repeates
    # first [10-15, 25-15, 5-25] = [5, 10, -20]
    # second [10-5, -20-10]
diff2 = np.diff(arr, n=2) # equivelent to [10-15, 25-15, 5-25]
print(diff2)

**Lowest Common Multiple** and **Greatest Common Denominator**

LCM - the least number that is common multiple of both of the numbers

GCD - the biggest number that is a common factor of both of the numbers


## LCM
# single elements
x = np.lcm(4, 6)
print(x)

# arrays
arr = np.array([3, 6, 9])
xx = np.lcm.reduce(arr)
print(xx)


## GCD
y = np.gcd(4, 6)
print(y)

arr2 = np.array([20, 8, 32, 36, 16])
yy = np.gcd.reduce(arr2)
print(yy)


**Unique elemets**

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])


a = np.unique(arr) # single array
b = np.union1d(arr, arr) # 2 arrays
c = np.intersect1d(arr1, arr2) # intersects of 2 arrays
d = np.setdiff1d(arr1, arr2) # values in arr1 not in arr2
e = np.setxor1d(arr1, arr2) # values not found in both

nu = [print(i) for i in [a, b, c, d, e]]


## Vectorisation


**`np.frompyfunc`**
* Takes an arbitrary Python function and returns a ufunc
* `frompyfunc(function, no. inputs, no. outputs)`

**`np.vectorize`**
* Evaluates pyfunc over input arrays using broadcasting rules of numpy, *convenience over performance*.
* wrapper for `frompyfunc`
* features: carries across docstring, defines broadcasting rules, and define dtype



def myMultiplier(x, y):
    return x * y

myMultiplier = np.frompyfunc(myMultiplier, 2, 1)

myMultiplier([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])


def myAdder(x, y):
    return x + y

myAdder = np.vectorize(myAdder)

myAdder([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
