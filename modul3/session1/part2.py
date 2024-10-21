# for loop

for letter in "Hello":
    print(letter)

# for number in 100:
#     print(number)

for number in range(1, 10, 2):
    print(number)

print(type(range(10)))
r = range(3)
gen = r.__iter__()
number = next(gen)
print(number)
number = gen.__next__()
print(number)
number = gen.__next__()
print(number)
# number = gen.__next__() - StopIteration - end loop
# print(number)

"abc".__iter__()
# (100).__iter__() - not iterable - not used in for loop


