check = int(input("Enter 1 to convert Farenheit to Celsius or 2 to convert Celsius to Fahrenheit: "))
if check == 1:
    F = float(input("Enter the temperature in Farenheit: "))
    C = (F - 32) * 5/9
    print(f"The temperature in Celsius is {C}.")
elif check == 2:
    C = float(input("Enter the temperature in Celsius: "))
    F = (C * 9/5) + 32
    print(f"The temperature in Farenheit is {F}.")
else:
    print("Invalid input. Please enter 1 or 2.")
    