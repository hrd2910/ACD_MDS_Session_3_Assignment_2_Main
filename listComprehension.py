# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

listCom = []
for letter in 'ACADGILD':
    listCom.append(letter)
print(listCom)



# Write List comprehensions to produce the following Lists
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]


matrix = [[2, 3, 4, 5],[3,4,5,6], [4,5,6,7],[5,6,7,8]]
transpose = [[row[i] for row in matrix] for i in range(4)]
print (transpose)


# Write List comprehensions to produce the following Lists
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

combs = []
for x in [1,2,3]:
        for y in [1,2,3]:       
             combs.append((x, y))
combs
