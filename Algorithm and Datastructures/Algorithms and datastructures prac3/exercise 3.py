"""Compute the value x**n for integer n."""
import matplotlib.pyplot as plt


def main():

    axis_limit = power(2, 18)+50000

    plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
             [power(2, 0), power(2, 1), power(2, 2), power(2, 3),
              power(2, 4), power(2, 5), power(2, 6), power(2, 7),
              power(2, 8), power(2, 9), power(2, 10), power(2, 11),
              power(2, 12), power(2, 13), power(2, 14), power(2, 15),
              power(2, 16), power(2, 17), power(2, 18)], 'ro')
    plt.axis([0, 19, 0, axis_limit])
    plt.show()


def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
    if n % 2 == 1:
        result *= x
    return result


main()
