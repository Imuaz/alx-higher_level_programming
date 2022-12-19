# 0x05. Python - Exceptions

In this project generally, I learn;
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

## Requirements :pushpin:

**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- code should use the [pycodestyle](https://alx-intranet.hbtn.io/rltoken/tgYt-0zVy1T4sDlE9ohxnA) (version `2.8.*`)
- All files must be executable
- The length of files will be tested using `wc`
## Tasks :page_with_curl:

**0. Safe list printing**
- [0-safe_print_list.py](./0-safe_print_list.py): python function that prints `x` elements of a list.
	- parameter  `my_list` can contain any type (integer, string, etc.)
	- All elements are printed on the same line followed by a new line.
	- `x` represents the number of elements to print
	- `x` can be bigger than the length of `my_list`
	- it returns the real number of elements printed
	- the use of `try: / except:` is mandatory
	- it is not allowed to import any module
	- the use of `len()` is not allowed

**1. Safe printing of an integers list**
* [1-safe_print_integer.py](./1-safe_print_integer.py): python function that prints an integer with `"{:d}".format()`.
  * the parameter `value` can be any type (integer, string, etc.)
	* The integer printed is followed by a new line
	* it returns `True` if `value` has been correctly printed (which means the `value` is an integer). Otherwise,it returns `False`
	* use of `try: / except:` is required
	* the `"{:d}".format()` is used to print as integer
	* it is not allowed to import any module
	* it is not allowed to use `type()`

**2. Print and count integers**

* [2-safe_print_list_integers.py](./2-safe_print_list_integers.py): python function that prints the first `x` elements of a list and only integers.
  * parameter `my_list` can contain any type (integer, string, etc.)
	* All integers are printed on the same line followed by a new line - other type of value in the list are skipped (in silence).
	* `x` represents the number of elements to access in `my_list`
	* `x` can be bigger than the length of `my_list` - if it’s the case, an exception occurs
	* it returns the real number of integers printed
	* `try: / except:` have been used as required
	* `"{:d}".format()` have been used to print an integer
	* no any module is imported as required
	* the `len()` is not used as required
	
**3. Integers division with debug**

* [3-safe_print_division.py](./3-safe_print_division.py): python function that divides 2 integers and prints the result.
 * parameters `a` and `b` are assumed to be integers
 * The result of the division is prints on the `finally:` section preceded by `Inside result:`
 * it returns the value of the division, otherwise: `None`
 * the`try: / except: / finally:` have been used
 * the `"{}".format()` have been used to print the result
 * it is not allowed to import any module

**4. Divide a list**

* [4-list_division.py](./4-list_division.py): python function that divides element by element 2 lists.
  - parameters `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
	- parameter `list_length` can be bigger than the length of both lists
	- it returns a new list (length = `list_length`) with all divisions
	- If 2 elements can’t be divided, the division result equals `0`.
	- If an element is not an integer or float:
	  - it prints: `wrong type`
  - If the division can’t be done (`/0`):
	  - it prints: `division by 0`
	- If `my_list_1` or `my_list_2` is too short
	  - it prints: `out of range`
	- the `try: / except: / finally:` have been used
	- it is not allowed to import any module

**5. Raise exception**

* [5-raise_exception.py](./5-raise_exception.py): python function that raises a type exception.
  - it is not allowed to import any module

**6. Raise a message**

* [6-raise_exception_msg.py](./6-raise_exception_msg.py): python function that raises a name exception with a message.
  - it is not allowed to import any module

**7. Safe integer print with error message**

* [100-safe_print_integer_err.py](./100-safe_print_integer_err.py): python function that prints an integer.
  - parameter `value` can be any type (integer, string, etc.)
	- The integer printed is followed by a new line
	- it returns `True` if `value` has been correctly printed (which means the `value` is an integer). Otherwise, it returns `False` and prints in `stderr` the error precede by `Exception:`
	- the `try: / except:` has been used as required
	- the `"{:d}".format()` has been used to print as integer
	- it is not allowed to use `type()`.

**8. Safe function**
* [101-safe_function.py](./101-safe_function.py): python function that executes a function safely.
  - it is assume that `fct` will be always a pointer to a function
	- it returns the result of the function,
	- Otherwise,it returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception:`
	- the `try: / except:` have been used as required

**9. ByteCode -> Python #4**

* [102-magic_calculation.py](./102-magic_calculation.py): python function `def magic_calculation(a, b):` that does exactly the same as the output Python bytecode given by ALX SE program.

**10. CPython #2: PyFloatObject**

* [103-python.c](./103-python.c):  C functions that print some basic info about Python lists, Python bytes an Python float objects.

## Files and Function prototypes :file_folder:

|File|Prototype|
|----|---------|
|`0-safe_print_list.py`|`def safe_print_list(my_list=[], x=0):`|
|`1-safe_print_integer.py`|`def safe_print_integer(value):`|
|`2-safe_print_list_integers.py`|`def safe_print_list_integers(my_list=[], x=0):`|
|`3-safe_print_division.py`|`def safe_print_division(a, b):`|
|`4-list_division.py`|`def list_division(my_list_1, my_list_2, list_length):`|
|`5-raise_exception.py`|`def raise_exception():`|
|`6-raise_exception_msg.py`|`def raise_exception_msg(message=""):`|
|`100-safe_print_integer_err.py`|`def safe_print_integer_err(value):`|
|`101-safe_function.py`|`def safe_function(fct, *args):`|
|`102-magic_calculation.py`|`def magic_calculation(a, b):`|
|`103-python.c`|`void print_python_list(PyObject *p);`, `void print_python_bytes(PyObject *p);`, `void print_python_float(PyObject *p);`|

