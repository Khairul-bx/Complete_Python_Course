

# # string creation ---------------------

s = 'khairul'
print(type(s))
print(s)

# # ord and chr ---------------------------


print(ord('a'))
print(ord('b'))

print(chr(102))
print(chr(100))


# # accessing substring -------------------------


name = 'khairul beex'
print(name[2])
print(name[-2])
print(name[2:6:1]) # start stop step


# # concatenation of string ------------------------


first_name = 'khairul'
last_name = 'kd'
sure_name = first_name + " " + last_name
print(sure_name)

num1 = 12
num2 = 15
print("Addition is : " + str(num1 + num2))

print("-" * 50)


# iterating over string ----------------------------


str1 = 'khairul'
for ch in str1:
    print(ch, end=" ")

Name = input("enter string : ")
print(len(Name))


str1 = input("enter strign : ")
vowel = ['a', 'b', 'c', 'd', 'e', 'A', 'E', 'I', 'O','U']
count = 0
for ch in str1:
    if ch in vowel:
        count += 1
print("Vowel : ", count)

name = 'khairul'
print(list(enumerate(name)))


# string method -----------------------------------


msg = 'hello, welcome'
print(msg.startswith('hello'))
print(msg.startswith('hello', 5, 11))

print(msg.endswith('me'))
print(msg.endswith('he', 5))

urls = ['https://www.khairulkd.com', 'https://www.beex.com']
for url in urls:
    url = url.lstrip('htps:/')
    print(url)

for url in urls:
    url = url.rstrip('htp.com')
    print(url)

result = [u.removeprefix('https://').removesuffix('.com') for u in urls]
print(result)

num = '-182'
name = 'khairul is a student'
rep = name.replace('khairul', 'kd')
print(rep)

print(name.find('khairul'))
print(name.rfind('xyz'))
print(name.index('i'))
print(name.count('i'))

print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.islower())
print(name.isupper())
print(name.lower())
print(name.upper())

print(name.capitalize())
print(name.title())
print(name.istitle())
print(name.center(25, '!'))
print(num.zfill(8))


# string formatting ---------------------------


name = input("enter name : ")
age = int(input("enter age : "))
print("name is %s and age is %d" % (name,age))
print(f"name is {name} and age is {age}")

msg = "heey bro beex"
res = msg.split()
print(res)
for ch in msg:
    print(ch.split(','), end="")

ls1 = ['A', 'B', 'C']
string = ''.join(ls1)
print(string)