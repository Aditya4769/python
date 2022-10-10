first = int(input("Enter Your First Number: "))
sign = input("Enter Your sign, [+, -, *, /, %]: ")
second = int(input("Enter Your Second Number: "))


if sign=="+" :
    print(first+second)
elif sign=="-":
    print(first-second)
elif sign=="*":
    print(first*second)
elif sign=="/":
    print(first/second)
elif sign=="%":
    print(first%second)
else:
    print("Invalid Number...")