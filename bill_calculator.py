print("There is a standard 2% tax fee and a 5% service charge.")
amount = float(input("Enter your bill amount: "))
if amount >= 5000:
    print("You are eligible for a 5% discount ")
    final = amount*1.02
    print(f"After applying taxes and discounts, your final amount is {final}")
else:
    final = amount*1.07
    print(f"After applying taxes, your final amount is {final}")


