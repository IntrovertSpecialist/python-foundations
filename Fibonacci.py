length = int(input("How many terms in the Fibonacci series? "))
a , b = 0 , 1
i = 0
for i in range(length):
    print(a)
    a , b = b , a + b
    i += 1