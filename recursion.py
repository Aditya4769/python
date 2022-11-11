# import sys
# def count():
#     print("hello world")
#     count()
#     limit = (sys.getrecursionlimit())
# count()
# #

# n = int(input("Enter your Number: "))
# def fact(n):
#     if n==0:
#         return 1
#     return n * fact(n-1)


# num = fact(n)
# print(num)

# n = int(input())
# def count(n):
   
#     return n**2
# num = count(n)
# print(num)



# x = lambda a: a*a
# num = x(5)

# print(num)

# a = int(input("Enter Your First Number: "))
# b = int(input("Enter Your Second Number: "))
# y = lambda a,b: (a+b)**2
# num = y(a,b)
# print(num)



def name(x,b,c):
    return lambda a: (a+x)*b*c
num = name(4,2,2)
print(num(5))