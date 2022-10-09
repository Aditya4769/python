import math
x = int(input("Enter First side of Triangle: "))
y = int(input("Enter Second Side of Triangle: "))
z = int(input("Enter Third Side of Triangle: "))
s = (x+y+z)/2
area = math.sqrt(s*(s-x)*(s-y)*(s-z))
print("The Area Of Triangle is: ",area)