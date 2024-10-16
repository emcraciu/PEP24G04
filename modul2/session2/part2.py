# # string methods
#
# var1 = """
# Hello1 TEST
# Python1
# """
# print(var1.split())
# print(type(var1.split()))
#
# result = var1.split()
# print(result[0])
# print(result[0:])
#
# result = '_'.join("abcd")
# print(result)
# print("_".join(var1.split()))

# id function

result = id('test')
print(result)
print(type(result))
print(hex(result))
# 0 1 2 3 4 5 6 7 8 9 a b c d e f > 10> 1f> 20> 2f ... > ff
print(bin(result))