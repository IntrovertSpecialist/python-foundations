marks = int(input("Enter your marks(out of 100): "))
if marks <= 100 and marks >= 0:
    if marks <=100 and marks > 90:
        print(f"You got {marks}% and your grade is A")
    elif marks <=90 and marks > 80:
        print(f"You got {marks}% and your grade is B")
    elif marks <=80 and marks > 70:
        print(f"You got {marks}% and your grade is C")
    elif marks <=70 and marks >= 60:
        print(f"You got {marks}% and your grade is D")
    elif marks < 60:
        print(f"You got {marks}% and your grade is F")
elif marks < 0:
    print(f"Your grade is F")
else:
    print("Invalid input, try again")
