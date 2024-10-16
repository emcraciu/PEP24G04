# print(r"/r\ ".center(7," "))
# print(r"//-\\".center(7," "))
# print("-------".center(7," "))
# print(r"\\-//".center(7," "))
# print(r"\-/".center(7," "))

# print()

# print("----".center(7," "))
# print(f"")


# print("*".center(9, " "))
# print("***".center(9, " "))
# print("*****".center(9, " "))
# print("*******".center(9," "))
# print(("*" * 9).center(9," "))

# str1 = "Hellow world"
# str1[0]
# str1[1]

# word = input("Introduceti un cuvant: ")
# result = word == word[::-1]
# print(f"palindrom: {result}")

# ------------------------------------------------------------------------------------------------------------
# string1 = "Hello Python"
# string2 = "Ana are mere"
# string3 = "Pizza Party"
#
# formatted_string1 = string1.replace(" ", "_")
# formatted_string2 = string2.replace(" ", "_")
# formatted_string3 = string3.replace(" ", "_")
#
# print(formatted_string1)
# print()
# print(formatted_string2)
# print()
# print(formatted_string3)

# ------------------------------------------------------------------------------------------------------------

# var1='Hello Python'
# print(var1[0:5],var1[6:], sep="_")
# print(var1.replace(" ","_"))
# split_words = var1.split()
# print("_".join(split_words))

# var2 = "Ana are mere"
#print(var2 + ".")
# print(f"{var2}.")

# var3 = "Pizza Party"
# split_words = var3.split()
# result = split_words[0] * 4
# print(result)

# (f"{var3}"[0:6] * 4)

# ------------------------------------------------------------------------------------------------------------

# var1 = "Hello Python"
# print(var1.split())
# print(type(var1.split()))
#
# result = var1.split()
# print(result[0])
#
# print("_".join(var1.split()))

# ------------------------------------------------------------------------------------------------------------

# id function
# result = id("test")
# print(result)
# print(type(result))
# print(hex(result))

a = 5.
b = 5
c = id("ana")


print("Locatia lui a este: ",hex(id(a)))
print("Locatia lui a este: ",hex(id(b)))
print("Locatia lui a este: ",hex(id(c)))

print(f"Tipul variabilei este: {type(a).__name__}")
print(f"Tipul variabilei este: {str(type(b)).split("'")[1]}")
print(f"Tipul variabilei este: {type(c)}")
print(f"Tipul variabilei este: {str(type(c)).split()[1][1:-2]}")