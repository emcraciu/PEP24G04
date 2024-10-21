# while loop

# while True:
#     number = input("give number")
#     print(f"Number is: {number}")

# while int(input("Give number: ")) < 100:
#     print("Number is to small")


# str1 = "Hello"
# # H e l l o
# # 0 1 2 3 4
# value = True
# index = 0
# while value:
#     letter = str1[index]
#     index += 1
#     print(letter)
#     if letter == 'e':
#         break
#     if index >= len(str1):
#         value = False
#
# print("done")

str1 = "Hello"
index = 0
while True:
    letter = str1[index]
    index += 1
    if letter == 'l':
        continue
    print(letter)
    if index >= len(str1):
        break
