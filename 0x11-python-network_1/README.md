# 0x11. Python - Network #1:earth_americas:

**INTRODUCTION**

The project covered several topics related to fetching internet resources and manipulating data using Python packages. It included an explanation of how to fetch internet resources using the `urllib` package and decode the body response. Additionally, it covered the usage of the `requests` package, highlighting its simplicity compared to `urllib`. The project also provided guidance on making HTTP requests, including `GET`, `POST`, `PUT`, and other methods. It further explained how to fetch JSON resources and manipulate data from external services. Overall, this project provided a comprehensive understanding of utilizing Python packages to interact with internet resources and manipulate data effectively.

## Resources:books:
***Read or watch***
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
- [Requests package](https://pypi.org/project/requests/)

## Requirements:pushpin:

**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A [README.md](../README.md) file at the root of the repo, containing a description of the repository
- A mandatory [README.md](./README.md) file, at the root of the folder of this project.
- the code should use the pycodestyle (version `2.8.*`)
- All the files must be executable
- The length of the files will be tested using `wc`
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get) must be used to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- the code should not be executed when imported (by using `if __name__ == "__main__":`)

## Tasks:page_witg_curl:

**0. What's my status? #0**
- [0-hbtn_status.py](./0-hbtn_status.py): A Python script that fetches `https://alx-intranet.hbtn.io/status`
  - it uses the package `urllib`
  - it is not allowed to import any packages other than `urllib`
  - it uses `with` statement
  - The body of the response should be displayed like the example below (tabulation before `-`)
  ```
  guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
  Body response:$7
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
  guillaume@ubuntu:~/0x11$
  ```
**1. Response header value #0**
- [1-hbtn_header.py](./1-hbtn_header.py): A Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
  - it uses the packages `urllib` and `sys`
  - it is not allow to import packages other than `urllib` and `sys`
  - The value of this variable is different for each request
  - No need to check arguments passed to the script (number or type)
  - it uses `with` statement

**2. POST an email #0**
- [2-post_email.py](./2-post_email.py): A Python that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)
  - the email will be sent in the `email` variable
  - it use the packages `urllib` and `sys`
  - it is not allowed to import packages other than `urllib` and `sys`
  - No need to check arguments passed to the script (number or type)
  - it uses the `with` statement

**3. Error code #0**
- [3-error_code.py](./3-error_code.py): A Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).
  - it manages `urllib.error.HTTPError` exceptions and prints: `Error code:` followed by the HTTP status code
  - it uses the packages `urllib` and `sys`
  - it is not allowed to import other packages than `urllib` and `sys`
  - No need to check arguments passed to the script (number or type)
  - it uses the `with` statement

**4. What's my status? #1**
- [4-hbtn_status.py](./4-hbtn_status.py): A Python script that fetches `https://alx-intranet.hbtn.io/status`
  - it uses the package `requests`
  - it is not allow to import packages other than `requests`
  - The body of the response should be display like the example below (tabulation before `-`)
  ```
  guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
  Body response:$
    - type: <class 'str'>$
    - content: OK$
  guillaume@ubuntu:~/0x11$ 
  ```

**5. Response header value #1**
- [5-hbtn_header.py](./5-hbtn_header.py): A Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
  - it uses the packages `requests` and `sys`
  - it is not allowed to import other packages than `requests` and `sys`
  - The value of this variable is different for each request
  - No need to check script arguments (number and type)

**6. POST an email #1**
- [6-post_email.py](./6-post_email.py): A Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.
  - The email should be sent in the variable `email`
  - it uses the packages `requests` and `sys`
  - it is not allowed to import packages other than `requests` and `sys`
  - No need to error check arguments passed to the script (number or type)

**7. Error code #1**
- [7-error_code.py](./7-error_code.py): A Python script that takes in a URL, sends a request to the URL and displays the body of the response.
  - If the HTTP status code is greater than or equal to 400, it prints: `Error code:` followed by the value of the HTTP status code
  - it uses the packages `requests` and `sys`
  - it is not allowed to import packages other than `requests` and `sys`
  - No need to check arguments passed to the script (number or type)

**8. Search API**
- [8-json_api.py](./8-json_api.py): A Python script that takes in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
  - The letter should be sent in the variable `q`
  - If no argument is given, it sets `q=""`
  - If the response body is properly JSON formatted and not empty, it displays the `id` and `name` like this: `[<id>] <name>`
  - Otherwise:
    - Displays `Not a valid JSON` if the JSON is invalid
    - Displays `No result` if the JSON is empty
  - it uses the package `requests` and `sys`
  - it is not allowed to import packages other than `requests` and `sys` 

**9. My GitHub!**
- [10-my_github.py](./10-my_github.py): A Python script that takes a GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users?apiVersion=2022-11-28) to display the `id`
  - it uses [Basic Authentication](https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api?apiVersion=2022-11-28) with a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to access the information (only `read:user` permission is needed)
  - The first argument will be `username`
  - The second argument will be `password` (in this case, a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))
  - it uses the package `requests` and `sys`
  - it is not allowed to import packages other than `requests` and `sys`
  - No need to check arguments passed to the script (number or type)

**10. Time for an interview!**
- The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```
- Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.
- [100-github_commits.py](./100-github_commits.py): A Python script that takes 2 arguments in order to solve this challenge.
  - The first argument will be the `repository name`
  - The second argument will be the `owner name`
  - it use the packages `requests` and `sys`
  - it is not allowed to import packages other than `requests` and `sys`
  - No need to check arguments passed to the script (number or type)

**Be careful: only 60 requests by hour by IP for unauthenticated requests**[Rate limit](https://docs.github.com/en/rest?apiVersion=2022-11-28).

   :+1:
