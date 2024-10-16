a = 5.
b = 5
c = 'ana'
print("Locatia lui a este: ", hex(id(a)))
print("Locatia lui b este: ", hex(id(b)))
print("Locatia lui c este: ", hex(id(c)))
print(f"Tipul variabilei a este: {str(type(a)).split("'")[1]}")
print(f"Tipul variabilei b este: {str(type(b)).split("'")[1]}")
print(f"Tipul variabilei c este: {str(type(c)).split("'")[1]}")
