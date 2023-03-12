l = [1,2,3,4,5]

# triangle
n = len(l)
for i in range(n):
    for j in range(i, n):
        l[i], l[j] = l[j], l[i]
print(l)


# reverse()
l1 = [1, 2, 3, 4, 5]

l1.reverse()
print(l1)

# using a loop through the original backward, append into a new copy
l2 = [1, 2, 3, 4, 5]
reversed_l = []
for i in range(len(l2)-1, -1, -1):
    reversed_l.append(l2[i])
l2 = reversed_l
print(l2)
