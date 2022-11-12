colors=["red","blue","green","yellow"]
cars = ["BMW","Ferrari","Buggati","Mahendra"]

# newlist = []
# for i in cars:
#     if "a" in i or "A" in i:
#         newlist.append(i)
#         print(i)
# print(newlist)

newlist = [i for i in cars if "a" in i or "A" in i]
newlist.sort(reverse=True)
print(newlist)