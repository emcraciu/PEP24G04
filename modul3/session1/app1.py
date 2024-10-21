cnp = input("Introduceti primele 7 cifre din CNP: ")
current_year = 2024
short_year = int(cnp[1:3])
print(short_year)
if cnp[0] == "1" or cnp[0] == "2":
    long_year = short_year + 1900
    print(long_year)
elif cnp[0] == "5" or cnp[0] == "6":
    long_year = short_year + 2000
else:
    print("CNP invalid ")
    exit()
age = current_year - long_year
print(age)
if age >= 18:
    print("Aveti peste 18 ani")
else:
    print("Nu aveti 18 ani")
