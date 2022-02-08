"""Compute the value x**n for integer n."""
import matplotlib.pyplot as plt


def main():

    result = power(2, 5)
    print(result)
    plt.plot([0, 1, 2, 3, 4, 5], [power(2, 0), power(2, 1), power(2, 2),
                                  power(2, 3), power(2,4), power(2, 5)], 'ro')
    plt.axis([0, 6, 0, 40])
    plt.show()


def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)


main()



