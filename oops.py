# class Laptop:
#     def config(self):
#         print("i3","1TB","12GB")
# laptop1 = Laptop()
# Laptop.config("1")
# laptop1.config()



# class Laptop:
#     def config():
#         print("i3","1TB","12GB")
# laptop1 = Laptop()
# Laptop.config()






# class A:
#     def __init__(self):
#         print("This is init of method A")

#     def method1(self):
#         print("This is method 1")

# class B:
#     def __init__(self):
#         # super().__init__()
#         print("This is init of method B")

#     def method2(self):
#         print("This is method  2")

# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print("This is init of method 3")

#     def method3(self):
#         print("This is method 3")

# objC = C()





# a = "Hello"
# b = (1,2,3,4)
# print(len(b))




# def add(a,b,c = 0):
#     return a+b+c
# print(add(1,2,3))
# print(add(1,2))





# # a = "Hello"
# # b = [1,2,3,4,5,6]

# # print(len(b))

# # def add(a,b,c = 0):
# #     return a+b+c

# # print(add(1,2))
# # print(add(1,2,3))


# class Rect:
#     def calculateArea(self, length = None, breadth = None):
#         if length != None and breadth != None:
#             return length * breadth
#         elif length != None:
#             return length * length

# rectangle = Rect()
# print(rectangle.calculateArea(2,3))
# print(rectangle.calculateArea(2))


# class Bird:
#     def category(self):
#         print("This is a category of bird")
    
#     def fly(self):
#         print("I can fly")


# class Sparrow(Bird):
#     def sizeParameter(self):
#         print("i am small in size")
# class Crow(Bird):
#     pass
# class Ostrich(Bird):
#     def fly(self):
#         print("I cannot fly, sorry")

# objBird = Bird()
# objSparrow = Sparrow()
# objCrow = Crow()
# objOstrich = Ostrich()

# objBird.category()
# objBird.fly()
# objCrow.category()
# objCrow.fly()
# objSparrow.category()
# objSparrow.fly()
# objOstrich.category()
# objOstrich.fly()










class vehicle:
    def capacity():
        print(4)

class car1(vehicle):
    pass
class car2(vehicle):
    pass
class bus(vehicle):
    def capacity():
        print(50)


objcar1 = car1
objcar2 = car2
objbus = bus

objcar1.capacity()
objcar2.capacity()
objbus.capacity()