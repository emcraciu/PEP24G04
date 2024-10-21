# if statement

if True:
    print("Working")

var1 = int(input("give number: "))
if var1 == 10:
    print(f"Working {var1}")
elif var1 == 11:
    pass
else:
    print(f"Not Working {var1}")

#  True and False objects

print(bool("abcd"))
print(bool(""))
print(bool(10))
print(bool(0+0j))
print(bool([]))

# if "abcd": ~ if True
# if "abcd"[1:2] ~ if True
# if []: ~ if False

# AND si OR

print(True and True)
print("Result off a and '' is: ", "a" and '')
print("Result off a or b is: ", "a" or 'b')
print("Result off a and b is: ", "a" and 'b')
print("Result off a and [] is: ", "a" and [])

