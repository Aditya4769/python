# set={"car","bike","train","car"}
# if 'bike' in set:
#     print("bike")
# else:
#     # print("none")



# set={"bike","train","car"}
# set.add("cycle")


# set={"bike","train","car"}
# set2={1,2,3}
# set.update(set2)
# print(set)



# set={"bike","train","car"}
# set.discard(" ")
# print(set)


# Error if given value not in variable
# set={"bike","train","car"}
# set.remove("")
# print(set)


# set={"bike","train","car"}
# del(set)
# print(set)




# set={"bike","train","car"}
# set1={1,2,3,4}
# set2={4,5,6,7}

# output=set2.union(set1)
# print(output)



set={"bike","train","car"}
set1={1,2,3,4}
set2={4,5,6,7}

output=set2.intersection(set1)
output1=set2.symmetric_difference(set1)
print(output)
print(output1)