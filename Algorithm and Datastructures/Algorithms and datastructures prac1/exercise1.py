"""
 (R-1.1) Write a short Python function, ​is_multiple​(​n, m),
 that takes two integer values and returns
 True if n is a multiple of m, that is, ​n=mi for some integer i
 and false otherwise
"""


def main():
    n = int(input("enter a number: "))
    m = int(input("enter another number: "))
    if is_multiple(n, m):
        print("true")
    else:
        print("false")


def is_multiple(n, m):
    return (n % m) == 0


main()
