# 0x00. Python - Hello, World:ocean:

**INTRODUCTION**

The project covers various aspects of Python programming, including its awesomeness and the creator of the programming language, Guido van Rossum. Additionally, it explains the origin of the name 'Python' and the philosophy behind the Zen of Python.

Furthermore, the project delves into the practical application of Python, providing a detailed understanding of how to use the Python interpreter, how to print text and variables using the print function, and how to use strings. It also covers indexing and slicing in Python, which is useful for manipulating strings.

In addition, the project explains the official Python coding style and how to check your code with `~~pycodestyle`. By the end of this project, It is expected to have a comprehensive understanding of Python programming, from its fundamentals to its practical applications and best practices.

## Resources:books:

The following are some resources used for the project:
- [The Python tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Guru](https://thepythonguru.com/)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program](https://youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Requirements:pushpin:

**Python Scripts**
- Allowed editors: `vi`, `vim`, `emacs`
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A [README.md](../README.md) file at the root of the repo, containing a description of the repository
- A mandatory [README.md](./README.md) file, at the root of the folder of this project.
- The code should use the pycodestyle (version `2.8.*`)
- All files must be executable
- The length of files is tested using `wc`

**Shell Scripts**
- Allowed editors: `vi`, `vim`, `emacs`
- All scripts are tested on Ubuntu 20.04 LTS
- All scripts should be exactly two lines long (`wc -l` file should print `2`)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- All files must be executable

**C Scripts**
- Allowed editors: `vi`, `vim`, `emacs`
- All files are compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All files should end with a new line
- The code should use the `Betty style`. It must be checked using `betty-style.pl` `and betty-doc.pl`
- the use of global variables is not Allowed
- No more than 5 functions per file
- The prototypes of all functions should be included in the header file called [lists.h](./lists.h)
- All header files should be include guarded

## More Info:information_source:

**Zen**
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
## Tasks:page_with_curl:
**0. Run Python file**
- [0-run](./0-run): Shell script that runs a Python script.
  - The Python file name will be saved in the environment variable `$PYFILE`

**1. Run inline**
- [1-run_inline](./1-run_inline): Shell script that runs Python code.
  - The Python code will be saved in the environment variable `$PYCODE`

**2. Hello, print**
- [2-print.py](./2-print.py): Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
  - it uses the function `print`

**3. Print integer**
- [3-print_number.py](./3-print_number.py): Python script that completes the [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line
  - it is not allowed to cast the variable `number` into a string
  - the code is 3 lines long as required
  - it uses f-strings [tips](https://realpython.com/python-f-strings/)

**4. Print float**
- [4-print_float.py](./4-print_float.py): Python script that completes the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.
  - The output of the program should be:
    - `Float`:, followed by the float with only 2 digits
    - followed by a new line
  - it is not allowed to cast number to string
  - it uses f-strings

**5. Print string**
- [5-print_string.py](./5-print_string.py): Python script that completes the [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.
  - The output of the program should be:
    - 3 times the value of `str` followed by a new line
    - followed by the 9 first characters of `str` followed by a new line
  - it is not allowed to use any loops or conditional statement
  - the program should be maximum 5 lines long
