"""if True:
    [print("Working")]

var1 = int(input("Give nr: "))
if var1 == 10: #in python se returneaza o valoare "fals-ish"
    print("working 10")
elif var1 == 11:
    pass
else:
    print(f"Not working {var1}")"""

# print(bool("abcd"))
# print(bool(""))
# print(bool(10))
# print(bool(0+0j))
# print(bool([]))

# if "abcd": ~ if True
# if "abcd"[1:2]: ~if True
# if []: ~ if False

# AND si OR
# print(True and False)
# print("a" and "") # empty string
# print("Result of a or '' is: ", "a" and '')
# print("Result of a or 'b' is: ", "a" or 'b')
# print("Result of a and '' is: ", "a" and 'b')
# print("Result of a and [] is: ", "a" and [])

# Exercitiul 1 ----------------------------------------------------------------------------

"""cnp = input("Introduceti CNP: ")
current_year = 2024
short_year = int(cnp[1:3])
if short_year >= 0 and short_year <= 24:
    full_year = 2000 + short_year  # Pentru anii 2000-2024
else:
    full_year = 1900 + short_year  # Pentru anii 1900-1999

age = current_year - full_year
if age >= 18:
    print("Ai peste 18 ani")
else:
    print("Nu ai inca 18 ani. Marsh la scoala")"""

cnp = input("Introduceti CNP: ")
current_year = 2024
short_year = int(cnp[1:3])
if cnp[0]== "1" or cnp[0]== "2":
    long_year = short_year + 1900
    # print(long_year)
elif cnp[0]== "5" or cnp[0]== "6":
    long_year = short_year+2000
else:
    print("CNP invalid")
    exit()
age = current_year - long_year
print(age)
if age >= 18:
    print("Aveti peste 18 ani.")
else:
    print("Nu aveti 18 ani.")