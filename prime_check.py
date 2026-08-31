n = int(input("Enter your number: "))
i = 2
if n == 1 or n == 0:
    print("Cannot say")
elif n < 0 :
    print("Negative numbers cannot be classified as prime numbers")
else:
    while i < n:
        if n % i != 0:
            i += 1
        else:
            print("Not a prime number") 
            exit()
    print("Prime Number")