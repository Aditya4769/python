years = int(input("Enter Your Service year: "))
salary = int(input("Enter your current salary: "))
if years>=10:
    print(((10/100)*salary)+(salary) , "Your bonus")
elif years>=6 and years<10:
    print((8/100)*salary, "your bonus")
elif years<6:
    print((5/100)*salary, "your bonus")
else:
    print("NO bonus")