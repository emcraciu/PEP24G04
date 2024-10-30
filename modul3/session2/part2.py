# set

my_set1 = set()  # empty set
my_set2 = {1, 3, 5, 5}
print(my_set1)
print(my_set2)
print(type(my_set1))

# operations with sets

my_set1.update([4, 5])
print(my_set1)
my_set1.update((9,))
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.difference(my_set2))
print(my_set1.symmetric_difference(my_set2))
print(my_set1.intersection_update(my_set2))
print(my_set1)
