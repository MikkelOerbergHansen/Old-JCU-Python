"""
The n-th harmonic number is the sum of the reciprocals of the first n natural numbers.
 For example, H​3​ = 1 + ½ + ⅓ = 1.833.
 A simple Python function for creating a list of the first n harmonic numbers follows:
"""


def main():
    n = int(input("Choose n: "))
    print("first a list")
    print(harmonic_list(n))
    print("now a generator")
    for i in harmonic_gen(n):
        print(i)


def harmonic_gen(n):
    num = 1
    for i in range(1, n+1):
        yield num
        num += 1 / (i+1)


def harmonic_list(n):
    result = []
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
        result.append(h)
    return result


main()
