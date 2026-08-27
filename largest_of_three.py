num = []
i = 0
for i in range(3):
    value = int(input(f"Enter number {i}:"))
    num.append(value)
    i += 1
largest = max(num)
smallest = min(num)
if num[0] == num[1] == num[2]:
    print("All the numbers are equal")
else:
    print(f"{largest} is the largest of the three and {smallest} is the smallest")


