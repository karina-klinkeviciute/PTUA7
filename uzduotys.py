
# Exercise 1: Reverse the tuple

tuple1 = (10, 20, 30, 40, 50)

# turim gauti rezultatą:

# (50, 40, 30, 20, 10)

# apsukimas su dvitaskiais
reversed_tuple = tuple1[::-1]

print(reversed_tuple)

# apsukimas su reveresed
tuple2 = (1, 2, 3, 4, 5)
reversed_tuple = tuple(reversed(tuple2))
print(reversed_tuple)

# tuples skaidymas

trumpas_tuple = tuple1[::-2]

print(trumpas_tuple)
