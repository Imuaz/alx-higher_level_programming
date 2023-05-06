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

**2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**
- [2-print_alphabet.py](./2-print_alphabet.py): a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
  - It uses only one `print` function with string format
  - the code uses only one loop
  - It is not allowed to store characters in a variable
  - It is not allowed to import any module

**3. When I was having that alphabet soup, I never thought that it would pay off**
- [3-print_alphabt.py](./3-print_alphabt.py): a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
  - It prints all the letters except `q` and `e`
  - it use only one `print` function with string format
  - the code uses only one loop
  - it does not store characters in a variable
  - no any module is imported

**4. Hexadecimal printing**
- [4-print_hexa.py](./4-print_hexa.py):a program that prints all numbers from `0` to `98` in decimal and in hexadecimal.
  - It uses only one `print` function with string format
  - it only uses one loop
  - it does not store numbers or strings in a variable
  - no any module is imported

**5. 00...99**
- [5-print_comb2.py](./5-print_comb2.py):a program that prints numbers from `0` to `99`.
  - Numbers are separated by `,`, followed by a space
  - Numbers are printed in ascending order, with two digits
  - The last number is followed by a new line
  - It uses not more than 2 `print` functions with string format
  - it uses only one loop
  - it does not store numbers or strings in a variable
  - no any module is imported

**6. Inventing is a combination of brains and materials. The more brains you use, the less material you need**
- [6-print_comb3.py](./6-print_comb3.py): a program that prints all possible different combinations of two digits.
  - Numbers are separated by `,`, followed by a space
  - The two digits must be different
  - `01` and `10` are considered the same combination of the two digits `0` and `1`
  - it prints only the smallest combination of two digits
  - Numbers are printed in ascending order, with two digits
  - The last number is followed by a new line
  - it uses not more than 3 `print` functions with string format
  - it uses not more than 2 loops
  - it does not store numbers or strings in a variable
  - no any module is imported

**7. islower**
- [7-islower.py](./7-islower.py): a function that checks for lowercase character.
  - Prototype: `def islower(c):`
  - it returns `True` if `c` is lowercase and `False` otherwise
  - no any module is imported
  - it does not use `str.upper()` and `str.isupper()`
  - no need to understand `__import__`
  - [Tips:ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

**8. To uppercase**
- [8-uppercase.py](./8-uppercase.py):a function that prints a string in uppercase followed by a new line.
  - Prototype: `def uppercase(str):`
  - it uses not more than 2 `prin`t functions with string format
  - it uses only one loop
  - no any module is imported
  - it does not use `str.upper()` and `str.isupper()`
  - no need to understand `__import__`
  - Tips:`ord()`

**9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important**
- [9-print_last_digit.py](./9-print_last_digit.py):a function that prints the last digit of a number.
  - Prototype: `def print_last_digit(number):`
  - it returns the value of the last digit
  - no any module is imported.
  - no need to understand `__import__`

**10. a + b**
- [10-add.py](./10-add.py): a function that adds two integers and returns the result.
  - Prototype: `def add(a, b):`
  - it returns the value of `a + b`
  - no any module is imported

**11. a ^ b**
- [11-pow.py](./11-pow.py):a function thatcomputes `a` to the power of `b` and return the value.
  - Prototype: `def pow(a, b):`
  - it returns the value of `a ^ b`
  - no any module is imported

**12. Fizz Buzz**
- [12-fizzbuzz.py](./12-fizzbuzz.py): a function that prints the numbers from `1` to `100` separated by a space.
  - For multiples of three, it prints `Fizz` instead of the number and for multiples of five, it  prints `Buzz`.
  - For numbers which are multiples of both three and five, it prints `FizzBuzz`.
  - Prototype: `def fizzbuzz():`
  - Each element is followed by a space
  - no any module is imported

**13. Insert in sorted linked list**
- [13-insert_number.c](./13-insert_number.c): C function that inserts a number into a sorted singly linked list.
  - it returns the address of the new node, or `NULL` if it failed
  - It use a header file [lists.h](./lists.h) that contains the prototype and struc of the function.

|File|Prototype/Struc|
|----|---------------|
|`13-insert_number.c`|`listint_t *insert_node(listint_t **head, int number);`
 ||`struct listint_s`|

**14. Smile in the mirror**
- [100-print_tebahpla.py](./100-print_tebahpla.py): a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
  - it uses only one `print` function with string format
  - it uses only one loop in
  - it does not store characters in a variable
  - no any module is imported.

**15. Remove at position**
- [101-remove_char_at.py](./101-remove_char_at.py): a function that creates a copy of the string, removing the character at the position `n` (not  int the Python way, the “C array index”).
  - Prototype: `def remove_char_at(str, n):`
  - no any module is imported

**16. ByteCode -> Python #2**
- [102-magic_calculation.py](./102-magic_calculation.py): Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:

```
3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
  - [tips - ByteCode](https://docs.python.org/3.4/library/dis.html)
