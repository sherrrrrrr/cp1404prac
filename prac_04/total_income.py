def main():
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = get_income_input(month)
        incomes.append(income)

    print_income_report(num_months, incomes)


def get_income_input(month):
    return float(input(f"Enter income for month {month}: "))


def print_income_report(months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


if __name__ == '__main__':
    main()