# strings

string1 = u"Hello World {}"
string2 = r'\n\tHello World\n'
print(string2)
string3 = """
    Hello World
"""
string4 = '''Hello World'''

# format method
string1 = "Hello World {}"
result = string1.format("Test")
print(result)

string1 = "Hello World {1}, {1}, {0}"
result = string1.format("Test0", 'Test1', 'Test2')
print(result)

string1 = "Hello World {test1}, {test2}, {test3}"
result = string1.format(test1="Test0", test2='Test1', test3='Test2')
print(result)

# formated string
var1 = input("Add to message: ")
var2 = "End"
string1 = f"Hello World {var1} {var1} {var2}"
print(string1)


# string length
var1 = "Hello World"
print(len(var1))
print(type(len(var1)))
result = len(var1)
print(f"len(var1)={len(var1)}, {var1.__len__()}, {result}")
