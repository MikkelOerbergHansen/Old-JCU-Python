"""
Exceptions

Answer the following questions:
1. When will a ValueError occur?
   - When numerator or denominator is not an integer
2. When will a ZeroDivisionError occur?
   - when denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes with a while loop checking for the error
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("ERROR!!! denominator can not be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
    pass
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
