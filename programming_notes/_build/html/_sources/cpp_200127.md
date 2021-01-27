# C++

## Basic script

`#include <iostream>` - header file, adds functionality

`using namespace std` - standard library

`count` is an object and the insertion operator (`<<`) is used to print text

```cpp
#include <iostream>
using namespace std;

int main()
{
	cout << "Hello World!";
	return 0;
}
```

## Compiling

- generate the output file: `g++ file.cpp`
- running `./a.out` will execute the program
- `g++  myfirstprogram.cpp -o myfirstprogram.o` will rename the output file
- Most IDEs will automatically do this, rename, and run the code
- VSCode: `cmd + shift + B`
- `gcc` is used for C

## Variables

`int` `double` `char` `string` `bool`

`char` - single quote

`string` - double quotes

**Declaring**

`type variable = value`

eg. `int myNum = 1;`

multiple declarations `int six = 6, seven = 7, eight = 8;`

`const` denotes a constant variable

`const int myNum = 6;`

## User input

`cin` reads data from keyboard and the extractor `>>` is used to assign it to a variable

`getline(cin, userTextIn);` allows for multiple words to be input

## Operations

The common ones are the same: `+` `-` `*` `/` `%` 

Incrementation is `++x` and `--x` 

**Assignments** 

`=` `+=` `-=` etc. 

there are many types of assignments of operators

**Logical**

`&&` - and

`||` - or

`!` - not

## Strings

`#include <string>` must be used for strings

*concatenation*: `stringOne + stringTwo`

*append*: `stringOne.append(stringTwo)`

length `stringOne.length()`

## Math

lots of functions - [https://www.w3schools.com/cpp/cpp_math.asp](https://www.w3schools.com/cpp/cpp_math.asp)

## If...else

syntax is similar to `R` 

```cpp
#include <iostream>
using namespace std;

int main()
{

	int numberOne = 200;
	int numberTwo = 22;
	if (numberOne == numberTwo)
	{
		cout << "true, they are equals ";
	}
	else if (numberTwo < numberOne)
	{
		cout << "number two is less than number one";
	}
	else
	{
		cout << "false, they are not equal";
	}
}
```

## Switch

don't use these...it's only here for reference

```cpp
switch (month)
	{
	case 1:
		cout << "Jan";
		break;
	case 2:
		cout << "Feb";
		break;
	case 3:
		cout << "Mar";
		break;
	default:
		cout << "It's a month alright...\n";
	}

	return 0;
```

## Loops

### while

```cpp
int counter = 0;

	while (counter <= 5)
	{
		cout << counter << "\n";
		counter++;
	}
```

### do/while

```cpp
int counter = 0;
do
	{
		cout << counter << "\n";
		counter++;
	} while (counter < 3);
```

### for

`for(statement1; statement2; statement3){}`

`statement1` - execute once before the code block

`statement2` - defines the conditions

`statement3` - executed after the code block has executed

```cpp
for (int i = 0; i < 5; i++)
	{
		cout << i << "\n";
	}
```

## Arrays

when initiating the array the number of elements must be specific

```cpp
string animals[3] = {"lion", "slug", "fish"};

// can be longer, just not shorter
string animals[5] = {"lion", "slug", "fish"};

// below will result in a length 3
string animals[] = {"lion", "slug", "fish"};

//or empty
string animals[5];
animals[1] = "lion";
animals[2] = "slug";
```

to ***count the number of elements in an array*** the number of allocated **bytes** is divided by the **number of bytes of that data type**

eg. 

```cpp
string animals[3] = {"lion", "slug", "fish"};

sizeof(animals) / sizeof(animals[0])
```

## References

the idea that a new variable is a reference of an existing one

uses `&`

it is also a soft copy, meaning that if the original is changed so is the link

the importance, becomes more apparent with *pointers*

```cpp
#include <iostream>
using namespace std;

int main()
{

	string food = "Pizza";
	cout << food << "\n";

	//reference
	string &meal = food;
	cout << meal << "\n";

	//it is a soft copy
	food = "eggs";
	cout << meal << "\n";
}
```

It can be used to access the memory address

```cpp
string food = "Pizza";
cout << &food << "\n"; // displays memory address
```

## Pointers

pointers store the memory address as the value

this becomes helpful when the **data is large**

rather than passing the data around (memory intensive), you pass its location

only single variables can be stored at the memory location ,

`*` is used 

```cpp
#include <iostream>
using namespace std;

int main()
{
	string animal = "slug";
	string *animalPtr = &animal;

	//output value
	cout << animal << "\n";

	//output memory address
	cout << &animal << "\n";

	//output memory address with the pointer
	cout << animalPtr << "\n";

	//dereference pointer
	cout << *animalPtr << "\n";

	//modify the pointer (and thus the original value)
	*animalPtr = "fire ant";
	cout << animal << "\n";
	cout << *animalPtr << "\n";

	return 0;
}
```

*dereference* -  returns the values stored at the memory address

*modifying* - changes the original value stored at that memory location

## Memory usage

We can assign and clear memory with the use of `new` and `delete` 

> The new operator should only be used if the data object should remain in memory until delete is called

This is a ***heap*** allocation method. i.e. not on the stack

The `delete` operator deallocates memory and calls the destructor for a single object created with `new`.

The `delete []` operator deallocates memory and calls destructors for an array of objects created with `new []`.

```cpp
#include <iostream>
using namespace std;

int main()
{
	int *pointerVar;

	//allocate memory
	pointerVar = new int;

	//assign
	*pointerVar = 45;

	//desired command
	cout << *pointerVar << "\n";

	//deallocate the memory
	delete pointerVar;

	return 0;
}
```

## Stack vs Heap

2 different methods of allocating memory

*pointers allocate via the heap*

**Stack** 

- the pointer moves the number of bytes we desire, so all memory is stored close together
- it's literally just stacking on top of one another
- this makes allocating very fast
- once out of the scope memory is free
- local
- Can fill up

**Heap**

- Allocation is not necessarily near each other
- Memory is retained until it is manually cleared
- many more steps when compiling, thus it takes longer to compute
- global
- Heap doesn't have any limit on memory size.

> Allocate memory on the stack, unless you can't 

eg. the variable is very large, or you need it globally after the stack has been cleared

```cpp
#include <iostream>

class myClass
{
public:
	float x, y, z;
};

int main()
{

	// -------
	// stack
	// -------
	int svalue = 5;	 //int
	int sarray[5];	 //array
	myClass svector; //object

	// -------
	// heap
	// -------

	//int
	int *hvalue = new int;
	*hvalue = 5;

	// array
	int *harray = new int[5];

	//object
	myClass *hvector = new myClass();

	// clear up
	delete hvalue;
	delete[] harray;
	delete hvector;

	return 0;
}
```

## Functions

`main()` is used to execute a block of code

it is proceeded by a return value definition

*Return values definitions:*

`void` - function doesn't return value

`int` - returns an integer, hence `return 0`

`string` - returns string

*parts of the function*

***declaration*** - functions name, return type, and parameters

***definition*** - body of the function

**Defining a argument**

define the type

```cpp
void sayHelloUser(string userName)
{
	cout << "hello " << userName;
}
```

and add a default

```cpp
void sayHelloUser(string userName = "jacob")
{
	cout << "hello " << userName;
}
```

## Function Overloading

instead of writing two functions for different inputs, we can make a function take multiple types of input

```cpp
#include <iostream>
using namespace std;

// to function method
int additionInt(int x, int y)
{
	return x + y;
}

double additionDouble(double x, double y)
{
	return x + y;
}

// we can instead have

int addition(int x, int y)
{
	return x + y;
}

double addition(double x, double y)
{
	return x + y;
}

int main()
{
	cout << additionInt(10, 24) << "\n";
	cout << additionDouble(10, 24) << "\n";
	cout << addition(10, 24) << "\n";
	cout << addition(10.1, 24.2) << "\n";
	return 0;
}
```

## OOP

***access specifiers*** `public` `private` `protected` 

are used to specify the accessibility of members (attributes and methods) outside the class

```cpp
#include <iostream>
using namespace std;

class animal
{
public:
	string species;
	int weight;
};

int main()
{
	// create the object and assign values
	animal bear;
	bear.species = "Grizzly";
	bear.weight = 600;

	//print test
	cout << bear.species << "\n";
	cout << bear.weight << "\n";
	return 0;
}
```

### **Assigning methods**

Methods can be assigned ***inside*** and ***outside*** the class

**Inside method**

```cpp
class greetingInside
{
public:
	void sayHello()
	{
		cout << "Hello\n";
	}
};
```

**Outside method**

this can be done for variables also

```cpp
class greetingOutside
{
public:
	void sayGoodbye();
};

void greetingOutside::sayGoodbye()
{
	cout << "Goodbye\n";
}
```

## Constructors

a method that is called when the object is created

use the ***same name as the class*** followed by `()`

```cpp
#include <iostream>
using namespace std;

class speciesCreator
{
public:
	speciesCreator()
	{
		cout << "you have created a new species\n";
	}
};

int main()
{
	speciesCreator bear;
	return 0;
}
```

constructors can have parameters

which may be used to set default values

## Access specifiers

There are 3 access speifiers in C++:

1. `public` - accessible outside the class
2. `private` - not accessible outside the class
3. `protected` - not accessed from outside, but can be accessed in *inherited classes* 

By default, all members of a class are `private`

## Encapsulation

Encapsulation uses the `private` access specifier to ensure data is hidden from the user.

To read or modify the data, we therefore reuire a **get** and **set** method

It is good practice to use encapsulation, and thus the `private` specifier

```cpp
#include <iostream>
using namespace std;

class Employee
{
private:
	int salary;

public:
	void setSalary(int s)
	{
		salary = s;
	}

public:
	int getSalary()
	{
		return salary;
	}
};

int main()
{
	Employee jacob;
	jacob.setSalary(30000);
	cout << jacob.getSalary() << "\n";
	return 0;
}
```

## Inheritance

**Base class** - the parent

**Derived class** - the child

`:` is usd when defining a class

`class fish : public animal`

```cpp
#include <iostream>
using namespace std;

//parent class
class animal
{

public:
	string species;
	string habitat;
	int weight;
	void sayHello()
	{
		cout << "hello I am a " << species << "\n";
	}
};

//child class
class fish : public animal
{
public:
	int maxDepth;
};

int main()
{
	fish shark;
	shark.species = "Great White";
	shark.maxDepth = 100;
	shark.sayHello();
	cout << "Max depth (m) " << shark.maxDepth << "\n";

	return 0;
}
```

## Multiple Inheritance

```cpp
class fish : public animal,
						 public underwater
{
};
```

```cpp
#include <iostream>
using namespace std;

// parent
class animal
{
public:
	string species;
	string habitat;
	void sayHello()
	{
		cout << "hello I am a " << species << "\n";
	};
};

// another parent
class underwater
{
public:
	int maxDepth;
};

// child with 2 parents
class fish : public animal,
			 public underwater
{
};

int main()
{
	fish shark;
	shark.species = "Basking";
	shark.maxDepth = 30;
	shark.sayHello();
	cout << "Max depth " << shark.maxDepth << "\n";
	return 0;
}
```

## Protected

allows for access within the inheritance class

> mark it private unless you have a good reason not to

```cpp
#include <iostream>
using namespace std;

class employee
{
protected:
	int salary;
};

class programmer : public employee
{
public:
	int bonus;

	void setSalary(int s)
	{
		salary = s;
	}

	int getSalary()
	{
		return salary;
	}
};

int main()
{
	programmer jacob;
	jacob.setSalary(40000);
	jacob.bonus = 10;
	cout << "my salary is: " << jacob.getSalary() << "\n";
	cout << "and the bonus is: " << jacob.bonus << "\n";
	return 0;
}
```

## Polymorphism

Inherited attributes and methods can be modified

```cpp
#include <iostream>
using namespace std;

class animal
{
public:
	void speakLan()
	{
		cout << "This animal goes XXX\n";
	}
};

class pig : public animal
{
public:
	void speakLan()
	{
		cout << "This animal goes oink\n";
	}
};

class dog : public animal
{
public:
	void speakLan()
	{
		cout << "This animal goes woof\n";
	}
};

int main()
{
	dog rex;
	pig babe;
	rex.speakLan();
	babe.speakLan();
	return 0;
}
```

## C++ Files

`<ofstream>` - create and write files

`<ifstream>` - reads from files

`<fstream>` - create, read, and writes

As before we use the insertion operator `<<` 

in combination with `ofsteam` and `ifstream`

## Writing

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream animalFile("sandbox/animals.txt");

	animalFile << "badgers live in sets\n";
	animalFile << "monkeys live in trees\n";
	animalFile << "otters live by rivers\n";

	animalFile.close();
	return 0;
}
```

## Reading

uses `while` and `getline()`

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	string readTextIn;

	ifstream readFile("sandbox/animals.txt");

	while (getline(readFile, readTextIn))
	{
		cout << readTextIn << "\n";
	}

	readFile.close();

	return 0;
}
```

## Exceptions

`try` - define the test code

`throw` - custom error to be caught be `catch`

`catch` - execute this when an error is thrown

```cpp
#include <iostream>
using namespace std;

int main()
{
	try
	{
		int age = 15;
		if (age >= 18)
		{
			cout << "access granted";
		}
		else
		{
			throw(age);
		}
	}
	catch (int myNum)
	{
		cout << "access denied\n";
		cout << "Your age is: " << myNum << "\n";
	}

	return 0;
}
```