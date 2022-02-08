"""
intermediate exercise 1
Write a program that prompts the user for 5 numbers
and then stores each of these in a list called numbers.
The program should then output various interesting things,
as in the output below (green represents user input).
Note that you can use the functions min, max, sum and len,
and you can use the append method to add a number to a list.
"""


def main():

    numbers = []
    for i in range(5):
        number = int(input("input a Number: "))
        numbers.append(number)

    number_stats(numbers)


def number_stats(numbers):

    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    average = sum(numbers) / len(numbers)
    print("The average of the numbers is", average)


main()
