# 1. Se cere afișarea următoarelor șiruri pe ecran:
# a. Astăzi mă duc la “facultate”.
# b. /*\/*\*/*\/*\
#       Python
#    \./\./\./\./
# c. P y t h o n

"""string1 = "facultate"
print(string1)"""


# string2 = (r"""/*\/*\*/*\/*\
#           Python
#           \./\./\./\./""")
# print(string2)

"""width = 10
print("/*\\/*\\*/*\\/*\\".center(width))
print("Python".center(width))
print("\\./\\./\\./\\./".center(width))"""

"""string3 = "P y t h o n"
string4 = "P\ty\tt\th\to\tn"
print(string3)
print(string4)
print(' '.join("Python"))
print('\t'.join("Python"))"""
# ----------------------------------------------------------------

# Se cere input de la utilizator:
# a. Numele utilizatorului
# b. Varsta

"""nume_utilizator = input("introduceti numele: ")
varsta = input("Introduceti varsta: ")

print(nume_utilizator)
print(varsta)"""

# ----------------------------------------------------------------

# Creati un script care sa aibe output similar cu exemplul urmator:
# Cum te numesti? Ana
# Ce varsta ai? 22
# Ceau Ana! Deci te-ai nascut in 1999.

"""nume = input("nume: ")
varsta = int(input("varsta: "))
anul_nasterii = 2024 - varsta

print(f"Cum te numesti? {nume}")
print(f"Varsta? {varsta}")
print(f"Ceau {nume}. Deci te-ai nascut in {anul_nasterii}")"""

# ----------------------------------------------------------------

# Cereți input de la utilizator cu un șir și afișați lungimea șirului in 4 moduri:
# - Cu metoda format()
# - Prin metoda f” ”
# - Concatenare (+)
# - Cu virgula

ex_3 = input("Introduceti un sir: ")
print("lungimea firului este {}".format(len(ex_3)))