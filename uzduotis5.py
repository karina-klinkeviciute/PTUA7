# https://pynative.com/python-tuple-exercise-with-solutions/#h-exercise-1-reverse-the-tuple

# Swap two tuples in Python

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1

print(tuple1, tuple2)


# tuple dalis
tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[0:-2]

print(tuple2)


# elemento keitimas viduje tuple
tuple3 = ([0, 2, 4], {3, 6, 7})

tuple3[0][2] = 6
tuple3[1].add(9)
tuple3[1].add(8)


sarasas = [1, 2, 3, 4, 5]

sarasas.extend(tuple3)
print(sarasas)



# del tuple3[0][1]
print(tuple3)

# pagooglinti: python mutables vs immutables

