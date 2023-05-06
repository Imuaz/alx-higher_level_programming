# 0x01. Python - if/else, loops, functions :loop:

**INTRODUCTION**

The project covered a wide range of topics related to Python programming. It started with an explanation of why Python programming is awesome, followed by an explanation of the importance of indentation in Python. The project also covered how to use various control flow statements, such as `if`, `if...else`, `break`, `continue`, and `else` clauses on loops, as well as how to use comments to document code.

Furthermore, the project explained how to assign values to variables, use `while` and `for` loops, and how Python’s `for` loop differs from `C`'s. It also covered the use of the `pass` statement and `range` function, as well as an understanding of what a function is and how to use it. The project also explored the scope of variables and what a traceback is.

Lastly, the project covered the arithmetic operators in Python and how to use them.

## Resources:books:

- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [IndentationError](https://youtu.be/1QXOd2ZQs-Q)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn to Program 2 : Looping](https://youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Requirements:pushpin:

**Python Scripts**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A mandatory [README.md](./README.md) file, at the root of the folder of the project, should be provided
- The code should use the pycodestyle (version `2.8.*`)
- All files must be executable
- The length your files will be tested using `wc`

**C Scripts**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All files should end with a new line
- The code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
- It is not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all the functions should be included in a header file called `lists.h`
- the header file should be pushed to the repo
- The header files should be include guarded

## Tasks:page_with_curl:

**0. Positive anything is better than negative nothing**
- [0-positive_or_negative.py](./0-positive_or_negative.py): The completion of a [program](https://github.com/holbertonschool/0x01.py) that assigns a random signed number to the variable `number` each time it is executed.It prints whether the number stored in the variable `number` is positive or negative.
  - The variable `number` stores a different value every time this program runs
  - No need to understand what `import`, `random.randint` do.
  - The output of the program should be:
    - The number, followed by
      1. if the number is greater than 0: `is positive`
      2. if the number is 0: `is zero`
      3. if the number is less than 0: `is negative`
    - followed by a new line

**1. The last digit**
- [1-last_digit.py](./1-last_digit.py): The completion of the [program](https://github.com/holbertonschool/0x01.py) that assigns a random signed number to the variable `number` each time it is executed. It prints the last digit of the number stored in the variable `number`.
  - The variable `number` stores a different value every time this program runs
  - No need to understand what `import`, random.`randint` do. The line: `number = random.randint(-10000, 10000)` should not be changed.
  - The output of the program should be:
    - The string `Last digit of`, followed by
    - the number, followed by
    - the string `is`, followed by the last digit of `number`, followed by
      1. if the last digit is greater than 5: the string `and is greater than 5`
      2. if the last digit is 0: the string `and is 0`
      3. if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
    - followed by a new line
