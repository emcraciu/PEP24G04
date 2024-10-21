number = int(input("Introduceți un număr: "))

if number < 0:
    start = number
    end = 0
else:
    start = 0
    end = number
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)
