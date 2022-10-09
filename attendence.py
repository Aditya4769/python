classes = int(input("Enter Your total classes in semseter: "))
attendent = int(input("Enter you toatal calss attend by you: "))
percentage = ((attendent)/(classes))*100
if percentage>=75:
    print("Your are allow to take a exam.")
else :
    print("You are not allowed to take a exam")