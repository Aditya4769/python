 # def name(name,age):
 #     print(name)
 #     print(age)
 # name("Aditya",18)



 # def name(*args):
 #     for i in args:
 #         print(i)

 # name(1,2,3,4,5,6)


# def name(firstname="Garv",age=100):
#     print("My Name is "+firstname,"My Age is ",age)
# name("Atul")
# name("Garv",101)


# a = input("NAme:")
# def office(EmployeeName,Salary=10000):
#     print(EmployeeName,"Salary =",Salary)
# office(a,9000)
# office(a,15000)
# office("Bob")

def info(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
info("Aditya",age="18",Place="Uttar pradesh",num=8005243520)