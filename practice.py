l1 = [0, 2, 1, 1, 0, 1, 2, 2,4]
#acending order
l1.sort()
print(l1)

sl1 = set(l1)
l2 = list(sl1)
print(l2)

count = 0 
al3 = []

for j in l2:
    for i in l1: 
        if i == j:
            count += 1
    al3.append(count)
    count = 0

for num in range(len(al3)):
    print("Ocu of ",l2[num], " = ", al3[num])