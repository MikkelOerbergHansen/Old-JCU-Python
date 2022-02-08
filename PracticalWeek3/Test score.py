"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():

    score = float(input("Enter score: "))
    result = score_check(score)
    print(result)


def score_check(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


main()
