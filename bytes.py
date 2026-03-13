
# bytes ---------------------------------------


# data = [10, 20, 30, 40]
# b = bytes(data)
# print(b)

# for ele in b:
#     print(ele)
# print(bytes(5))


# bytes method ----------------------------------


# b.count()
# b.find()
# b.index()
# b.startswith()
# b.endswith()
# b.split()
# b.replace()


# bytesarray -------------------------------------


# data = [10, 20, 30, 40]
# b = bytearray(data)
# print(type(data))
# print(b)
# for ele in b:
#     print(ele)


# bytesarray method ----------------------------------


# b.append()
# b.extend()
# b.insert()
# b.pop()
# b.remove()
# b.reverse()


# Encoding ----------------------------------------


import sys
str1 = 'khairul'
print(sys.getsizeof(str1))

data = [65, 97, 98]
b = bytes(data)
print(b)
a = bytearray(data)
print(a)
print(sys.getsizeof(b))
name = bytes("khairul", encoding='utf-8')
print(name)


# decoding --------------------------------------


str1 = 'khairul'
b = bytes(str1, 'utf-8')
del str1

str2 = b.decode()
print(str2)