age1 = int(input("Enter Your Age: "))
age2 = int(input("Enter Your Age: "))
age3 = int(input("Enter Your Age: "))
if age1<age2 and age1<age3:
    print(age1, "is Youngest")
elif age2<age1 and age2<age3:
    print(age2, "is Youngest")
elif age3<age1 and age3<age2:
    print(age3, "is Youngest")

if age1>age2 and age1>age3:
    print(age1, "is oldest")
elif age2>age1 and age2>age3:
    print(age2, "is oldest")
else:
    print(age3, "is oldest")