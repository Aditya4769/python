x = int(input("Enter First side of Triangle: "))
y = int(input("Enter Second Side of Triangle: "))
z = int(input("Enter Third Side of Triangle: "))
s = (x+y+z)/2
area = (s*(s-x)*(s-y)*(s-z))**0.5
print("The Area Of Triangle is: ",area)