

def main():

    a = 5
    b = 5
    result = product(a, b)
    print(result)


def product(a, b):
    if b == 0:
        return 0
    else:
        return a + product(a, b-1)


main()
