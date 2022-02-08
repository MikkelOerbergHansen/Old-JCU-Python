"""
Calculating a List of Cumulative Totals (Read the whole question before starting the work!)
Accountant Annie wants you to write a program to calculate the monthly cumulative totals for incomes.
The program should ask for the number of monthly incomes to enter,
then get and store them in a list.
When the incomes have been entered,
the program should display a list of the month’s income next to the
cumulative income at that point - for each month. Here’s some sample output:
"""


def main():
    """Display income report for incomes over a given number of TotalMonths."""
    incomes = []
    total_months = int(input("How many Months? "))

    for month in range(1, total_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    income_report(incomes, total_months)


def income_report(incomes, total_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:7.2f} Total: ${:7.2f}".format(month, income, total))


main()
