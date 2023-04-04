# 0x10. Python - Network #0:globe_with_meridians:

The project covers various topics related to URLs and HTTP, starting with their definitions and moving on to their components, including scheme, domain name, sub-domain, port number, and query string. It also covers HTTP request and response components, including headers and message body, request methods, and response status codes. In addition, the project explains HTTP Cookies, making requests with cURL, and the application-level processes that occur when typing a URL into a browser. Overall, this project provides a comprehensive understanding of URLs and HTTP.

## Requirements :pushpin:

**General**

- Allowed editors: `vi`, `vim`, `emacs`
- A mandatory [README.md](./README.md) file, at the root of the folder of the project, is provided.
- All  scripts is tested on Ubuntu 20.04 LTS
- All Bash scripts are exactly 3 lines long (`wc -l file` should print 3)
- All files end with a new line
- All files are executable
- The first line of all the bash files are exactly `#!/bin/bash`
- The second line of all Bash scripts is a comment explaining what is the script doing
- All `curl` commands have the option `-s` (silent mode)
- All files is interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- The first line of your Python files is exactly `#!/usr/bin/python3`
- The code uses the pycodestyle (version `2.8.*`)
- All modules are documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All classes are documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All functions (inside and outside a class) is documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks :page_with_curl:

**0. cURL body size**
- [0-body_size.sh](./0-body_size.sh): Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
  - The size is displayed in bytes
  - the `curl` is used
  - the script is tested in the sandbox provided, using the web server running on port 5000

**1. cURL to the end**
- [1-body.sh](./1-body.sh): Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
  - it displays only the body of a `200` status code response
  - it uses the `curl`
  - the script is tested in the sandbox provided, using the web server running on port 5000

**2. cURL Method**
- [2-delete.sh](./2-delete.sh): Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response
  - it uses the `curl`
  - the script is tested in the sandbox provided, using the web server running on port 5000

**3. cURL only methods**
- [3-methods.sh](./3-methods.sh): Bash script that takes in a URL and displays all HTTP methods the server will accept.
  - it uses the `curl`
  - the script is tested in the sandbox provided, using the web server running on port 5000

**4. cURL headers**
- [4-header.sh](./4-header.sh): Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
  - A header variable `X-School-User-Id` is sent with the value `98`
  - it uses `curl`
  - the script is tested in the sandbox provided, using the web server running on port 5000

**5. cURL POST parameters**
- [5-post_params.sh](./5-post_params.sh): Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
  - A variable `email` is sent with the value `test@gmail.com`
  - A variable `subject` is sent with the value `I will always be here for PLD`
  - it uses `curl`
  - the script is tested in the sandbox provided, using the web server running on port 5000

**6. Find a peak**
- [6-peak.py](./6-peak.py): function that finds **a peak** in a list of unsorted integers.
  - it uses a prototype: `def find_peak(list_of_integers):`
  - it has not imported any module
  - The algorithm have the lowest complexity (No need to go through all numbers to find a peak)
  - the function contain in the file 6-peak.py
  - [6-peak.txt](./6-peak.txt) contain the complexity of the algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`

**
