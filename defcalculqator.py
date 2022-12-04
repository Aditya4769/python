x = int(input("Enter Your First Number: "))
y = int(input("Enter Your Second Number: "))
operator= input("Enter Your operator, [+, -, *, /, %, **, //]: ")
def count():
    if operator=="+" :
        print(x+y)


    elif operator=="-":
        (x-y)


    elif operator=="*":
        print(x*y)


    elif operator=="/":
        print(x/y)


    elif operator=="%":
        print(x%y)


    elif operator=="**":
        print(x**y)


    elif operator=="//":
        print(x//y)


    else:
        print("Invalid Number...")

count()