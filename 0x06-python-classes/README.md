# 0x06. Python - Classes and Objects

In this project, I generally learn about Python OOP, "first-class everythin", class, object, instance,the difference between class and object or instance, attribute; (how to use public, protected and private attributes), `self`, method, the special `__init__` method, Data Abstraction, Data Encapsulation, information Hiding, property, the difference between an attribute and a property in Python, the Pythonic way of writing getters and setters in Python, the way to dynamically create arbitrary new attributes for existing instances and class, How to bind attributes to object and classes,the `__dict__` of class and/or instance of a class and what does it contain, how Python find the attributes of an object or class and finally how to use the `getattr` function.

## Background Context :book:

During this project period, OOP(Object Oriented Programmin) was introduced as totally new concept for all ALX SE Students carrying out the project (especially those who think they know about it :)).Therefore,in order to easily understand the project it’s VERY important that a student should read at least all the material provided for the project that is listed bellow (and skip what was recommended for the student to skip,which was covered later in the curriculum).

As usual,it has been recomended thak a student should type (never copy and paste), test, understand all examples shown in the following links (including those in the video provided), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, and  play with it :)!

### Links to the Materials :bookmark_tabs:

It is recommended to read or watch the below resources in the order presented.
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) ( _Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes_, `classmethod` _and_ `staticmethod` _yet_ )
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) ( _Please_ **be careful**: _in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The_ ` __init__` _Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”_)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://youtu.be/1AGyBuVCTeE)
- [Python Classes and Objects](https://youtu.be/apACNr7DC_s)
- [Object Oriented Programming](https://youtu.be/-DP1i2ZU9gk)

## Requirements :pushpin:

**General**

* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* the code should use the pycodestyle (version `2.8.*`)
* All files must be executable
* The length of files will be tested using `wc`
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c` `'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### More Info :memo:
**Documentation is now mandatory!** Each module, class, and method must contain docstring as comments.[Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Taks :page_with_curl:

**0. My first square**
* [0-square.py](./0-square.py): An empty class `Square` that defines a square:
	- it is not allowed to import any module

**Square with size**
* [1-square.py](./1-square.py): a class `Square` that defines a square by: (based on `0-square.py`)
	- it has a private instance attribute: `size`
	- instantiation with `size` (no type/value verification)
	- it is not allowed to import any module
	
**2. Size validation**
* [2-square.py](./2-square.py): a class `Square` that defines a square by: (based on `1-square.py`)
	- it has a private instance attribute: `size`
	- instantiation with optional size: `def __init__(self, size=0):`
		- `size` must be an integer, otherwise it raises a `TypeError` exception with the message `size must be an integer`
		- if size is less than `0`, it raise a `ValueError` exception with the message `size must be >= 0`
	- it is not allowed to import any module
	
**3. Area of a square**
* [3-square.py](./3-square.py): a class `Square` that defines a square by: (based on `3-square.py`)
	- with a private instance attribute: `size`:
		- property `def size(self):` retrieves it
		- property setter `def size(self, value):` set it:
			- `size` must be an integer, otherwise it raises a `TypeError` exception with the message `size must be an integer`
			- if `size` is less than `0`, it raises a `ValueError` exception with the message `size must be >= 0`
	- Instantiation with optional `size`: `def __init__(self, size=0):`
	- Public instance method: `def area(self):` which returns the current square area
	- it is not allowed to import any module
	
**4. Access and update private attribute**
* [4-square.py](./4-square.py): a class `Square`  that defines a square by: (based on `3-square.py`)
	- with private instance attribute: `size`:
		- property `def size(self):` retrieves it
		- property setter `def size(self, value):` set it:
			- `size` must be an integer, otherwise it raises a `TypeError` exception with the message `size must be an integer`
			- if `size` is less than `0`,it raises a `ValueError` exception with the message `size must be >= 0`
	- Instantiation with optional `size`: `def __init__(self, size=0):`
	- Public instance method: `def area(self):` which returns the current square area
	- it is not allowed to import any module
	
**5. Printing a square**
* [5-square.py](./5-square.py): a class `Square` that defines a square by: (based on `4-square.py`)
	- with private instance attribute: `size`:
		- property `def size(self):`retrieves it
		- property setter `def size(self, value):` set it:
			- `size` must be an integer, otherwise it raises a `TypeError` exception with the message `size must be an integer`
			- if `size` is less than `0`, it raises a `ValueError` exception with the message `size must be >= 0`
	- Instantiation with optional `size`: `def __init__(self, size=0):`
	- Public instance method: `def area(self):` which returns the current square area
	- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
		- if `size` is equal to `0`, print an empty line
	- it is not allowed to import any module

**6. Coordinates of a square**
* [6-square.py](./6-square.py): a class `Square` that defines a square by: (based on `5-square.py`)
	- with private instance attribute: `size`:
		- property `def size(self):`retrieves it
		- property setter `def size(self, value):` set it:
			- `size` must be an integer, otherwise it raises a `TypeError` exception with the message `size must be an integer`
			- if `size` is less than `0`, it raisew a `ValueError` exception with the message `size must be >= 0`
	- with private instance attribute: `position`:
		- property `def position(self):` that retrieves it
		- property setter `def position(self, value):` set it:
		- `position` must be a tuple of 2 positive integers, otherwise it raises a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
	- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
	- Public instance method: `def area(self):` which returns the current square area
	- Public instance method: `def my_print(self):` which prints in stdout the square with the character `#`:
		- if `size` is equal to `0`, print an empty line
		- `position` is  use by using space **- Don’t fill lines by spaces** when `position[1] > 0`
	- no any module was imported as required

**7. Singly linked list**
* [100-singly_linked_list.py](./100-singly_linked_list.py): a class `Node` that defines a node of a singly linked list by:
	- Private instance attribute: `data`:
		- property `def data(self):` that retrieves it
		- property setter `def data(self, value):` set it:
			- `data` must be an integer, otherwise it raise a `TypeError` exception with the message `data must be an integer`
	- Private instance attribute: `next_node`:
		- property `def next_node(self):` that retrieves it
		- property setter `def next_node(self, value):` set it:
			- `next_node` can be `None` or must be a `Node`, otherwise it raise a `TypeError` exception with the message `next_node must be a Node object`
	- Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None):`

  And a class `SinglyLinkedList` that defines a singly linked list by:
	- Private instance attribute: `head` (no setter or getter)
	- Simple instantiation: `def __init__(self):`
	- printable that:
		- prints the entire list in stdout
		- one node number by line
	- Public instance method: `def sorted_insert(self, value):` which inserts a new `Node` into the correct sorted position in the list (increasing order)
	- no any module was imported as required

**8. Print Square instance**
* [101-square.py](./101-square.py): a class `Square` that defines a square by: (based on `6-square.py`)
	- with private instance attribute: `size`:
		- property `def size(self):` retrieves it
		- property setter `def size(self, value):` set it:
			- `size` must be an integer, otherwise it raises a `TypeError` exception with the message `size must be an integer`
			- if `size` is less than `0`,it raises a `ValueError` exception with the message `size must be >= 0`
	- Private instance attribute: `position`:
		- property `def position(self):` retrieves it
		- property setter `def position(self, value):` set it:
			- `position` must be a tuple of 2 positive integers, otherwise it raises a `TypeError` exception with the message `position must be a tuple of 2 positive integer`
	- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
	- Public instance method: `def area(self):` which returns the current square area
	- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
		- if `size` is equal to `0`,it prints an empty line
		- `position` is use by using space
	- Printing a `Square` instance have the same behavior as `my_print()`
	- no any module was imported as required

**9. Compare 2 squares**
* [102-square.py](./102-square.py): a class `Square` that defines a square by: (based on `4-square.py`)
	- with private instance attribute: `size`:
		- property `def size(self):`retrieves it
		- property setter `def size(self, value):` set it:
			- `size` must be a number (float or integer), otherwise it raises a `TypeError` exception with the message `size must be a number`
			- if `size` is less than `0`,it raises a `ValueError` exception with the message `size must be >= 0`
	- Instantiation with `size`: `def __init__(self, size=0):`
	- Public instance method: `def area(self):` which returns the current square area
	- `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area
	- no any module was imported as required

**10. ByteCode -> Python #5**
* [103-magic_class.py](./103-magic_class.py): Python class `MagicClass` that does exactly the same as a given Python bytecode given
