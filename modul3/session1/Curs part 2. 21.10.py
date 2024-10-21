# for loop

# for letter in "Hello":
#     print(letter)
#
# for number in range(1,10,2):
#     print(number)
#
# print(type(range(10))) # => result <class 'range'>

"""r = range(3)
gen = r.__iter__()
number = next(gen)
print(number)
number = gen.__next__()
print(number)
number = gen.__next__()
print(number)
# number = gen.__next__()   - fiind range 3 => StopIteration = end Loop
# print(number)"""
from tokenize import endpats

# "abc".__iter__()
# (100).__iter__()      => not iterable - not used in for_loops

# Exercitiu 2 --------------------
# Luați input de la utilizator un număr și parcurgeți intervalul de la 0 pana la numărul
# introdus de către utilizator, afisand toate numerele pare

number = int(input("Introduceti un numar: "))
if number < 0:
    start = number
    end = 0
else:
    start = 0
    end = number
for i in range(start, end + 1):
    if i % 2 == 0:  # Verificăm dacă numărul este par
        print(i)