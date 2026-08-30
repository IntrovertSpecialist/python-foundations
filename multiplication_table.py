n = int(input("Enter the number of rows for the multiplication table: "))
num = int(input("Enter the number for which you want the multiplication table: "))
for i in range(n):
    print(f"{num} x {i+1} = {num*(i+1)}\n")
    i += 1

