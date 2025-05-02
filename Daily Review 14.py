def exact_change(user_total):
    total = user_total
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    while total > 0:
        while total > 0:
            if total - 25 >= 0:
                num_quarters += (total // 25)
                total -= num_quarters * 25
            else:
                break
        while total > 0:
            if total - 10 >= 0:
                num_dimes += (total // 10)
                total -= num_dimes * 10
            else:
                break
        while total > 0:
            if total - 5 >= 0:
                num_nickels += (total // 5)
                total -= num_nickels * 5
            else:
                break
        if total % 25 != 0 and total % 10 != 0 and total % 5 != 0:
            num_pennies += (total // 1)
            total -= (num_pennies * 1)

    return num_pennies, num_nickels, num_dimes, num_quarters


input_val = int(input())
num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

if input_val <= 0:
    print("no change")

if num_pennies > 0:
    if num_pennies > 1:
        print(f"{num_pennies} pennies")
    elif num_pennies == 1:
        print(f"{num_pennies} penny")

if num_nickels > 0:
    if num_nickels > 1:
        print(f"{num_nickels} nickels")
    elif num_nickels == 1:
        print(f"{num_nickels} nickel")

if num_dimes > 0:
    if num_dimes > 1:
        print(f"{num_dimes} dimes")
    elif num_dimes == 1:
        print(f"{num_dimes} dime")

if num_quarters > 0:
    if num_quarters > 1:
        print(f"{num_quarters} quarters")
    elif num_quarters == 1:
        print(f"{num_quarters} quarter")