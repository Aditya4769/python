# def count(list):
#     even=0
#     odd=0

#     for i in list:
#         if i%2==0:
#             even += 1
#         else:
#             odd += 1
#     return even,odd


# list = [32,21,64,100,31]

# even,odd = count(list)
# print(even)
# print(odd)










def count(list):
    total=0
    for i in list:
        if len(i)<5:
            total = total+1
        else:
            total = total
    return total
list = ["Shubham","Atul","Anurag","Rahul","Dev","Roy"]
total=count(list)
print(total)