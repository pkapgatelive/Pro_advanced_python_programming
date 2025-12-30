# how to find the common number from the list

list = [1,2,3,4,5,6,7,8,9,10]

list_1 = [2,3,4,7,8,9,10]


intersection = []

for x in list:
    for y in list_1:
        if x == y:
            intersection.append(x)

print(intersection)


inter = [x for x in list if x in list_1]
print(inter)

inter_1 = [x for x in list for y in list_1 if x == y]
print(inter_1)