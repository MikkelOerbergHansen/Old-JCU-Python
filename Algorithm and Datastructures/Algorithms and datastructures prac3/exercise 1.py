

def main():
    seq = (5, 10, 15, 20, 6, 12)
    print(max_seq(seq))


def max_seq(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        m = max_seq(seq[1:])
        return m if m > seq[0] else seq[0]


main()
