
#if statement
is_hot = False
is_cold = False
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear a warm clothes")

else:
    print("It is a lovely day")
print("Enjoy your day")


price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

has_high_income = True
has_good_credit = True

if has_high_income and not has_good_credit:
    print('Eligible for the loan')
elif has_high_income or has_good_credit:
    print('get more income')
else:
    print('Not eligible for the loan')