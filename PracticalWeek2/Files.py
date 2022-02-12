"""
Files
note: when you execute a Python program that
contains a line like open('data.txt', 'w')
the new file “data.txt” is created in the same folder
as the Python file in your PyCharm project.
"""

# exercise 1
name = str(input("please enter your name: "))
out_file = open("PracticalWeek2/names.txt", 'w')
print(name, file=out_file)
out_file.close()
print("your name is printed to file")

print()
print()

# exercise 2
name_file = open("PracticalWeek2/names.txt", "r")
print("your name is retrieved from file")
name = name_file.read()
print("Your name is {}".format(name))
name_file.close()

print()
print()

# create number.txt
number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
out_file = open("PracticalWeek2/numbers.txt", 'w')
print(number1, file=out_file)
print(number2, file=out_file)
out_file.close()

# exercise 3
number_file = open("PracticalWeek2/numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
print("the sum of your two numbers is: {} ".format(number1 + number2))
number_file.close()

print()
print()

# input more numbers
number_count = int(input("how many numbers do you have? "))
number_file = open("PracticalWeek2/numbers.txt", "w")
for i in range(number_count):
    number = int(input("enter your number: "))
    print(number, file=number_file)
number_file.close()

# Exercise 4 : print sum of all numbers in a file
number_file = open("PracticalWeek2/numbers.txt", "r")
total = 0
for line in number_file:
    number = int(line)
    total += number
print("the sum of all your numbers is: {}".format(total))
number_file.close()
