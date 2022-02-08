"""
intermediate exercise 2
Woefully inadequate security checker…
Copy the following list of usernames into a new Python file:
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
            'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
            'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
"""


def main():

    username = input("Enter username:")

    status = security_check(username)
    while status == "Access denied":
        print(status)
        username = input("Enter username:")
        status = security_check(username)
    print(status)


def security_check(username):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    if username in usernames:
        return "Access granted"
    else:
        return "Access denied"


main()
