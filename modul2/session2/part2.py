# string methods

var1 = """
Hello1 TEST
Python1
"""
print(var1.split())
print(type(var1.split()))

result = var1.split()
print(result[0])
print(result[0:])

result = '_'.join("abcd")
print(result)
print("_".join(var1.split()))
