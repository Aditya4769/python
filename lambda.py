# x = lambda num1,num2: (num1+num2)
# print(x(3,4))


# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# a=filter(isEven,list1)
# print(list(a))


# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# a=filter(lambda i :i%2==0,list1)
# print(list(a))





# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# a=filter(lambda i :i>15,list1)
# print(list(a))





# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# a=map(lambda i :i+2,list1)
# print(list(a))




# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# a=map(lambda j :j**2,list1)
# print(list(a))




# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# a=map(lambda j :j**1.5,list1)
# print(list(a))




# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# a=map(lambda j :"{:.2f}".format(j**1.5),list1)
# print(list(a))





# from functools import reduce

# list1=[3,2,8,16,11,34,17]
# a=reduce(lambda a,b:a*b,list1)
# print(a)




list1=[34,88,30,22,10,15,18]
a=filter(lambda j :j%5==0,list1)
print(list(a))