"""
Mikkel Hansen
"""


def main():
    name = get_name()

    freq = int(input("input the frequency of letters to print: "))
    print_letters_of_freq(name, freq)


def get_name():
    name = str(input("input your name: "))
    status = error_check(name)
    while status != "Only alphabetical letters and spaces: yes":
        print(status)
        name = str(input("error!! input your name: "))
        status = error_check(name)
    print(status)
    return name


def error_check(name):
    if all(x.isalpha() or x.isspace() for x in name):
        return "Only alphabetical letters and spaces: yes"
    else:
        return "Only alphabetical letters and spaces: no"


def print_letters_of_freq(name, freq):
    for i in range(len(name)):
        if i % freq == 0:
            print(name[i], end=" ")


main()
