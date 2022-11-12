numbers=[1,2,3,4,5,2,6]
# c=0
# newlist=[]
# for i in numbers:
#     if i==2 and c==0:
#         newlist.append(200)
#         c = c+1
#     else:
#         newlist.append(i)
# print(newlist)
indx=numbers.index(2)
numbers[indx]=200
print(numbers)
