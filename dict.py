
# creating dictionary --------------------------------


student = {'name' : 'Khairul', 'roll' : 1052}
print(type(student))
print(student)

student = dict([('name ', 'khairul'), ('roll', 1053)])
print(student)

student = {}
student = dict()
print(student)

print(len(student))
count = 0
for key in student:
    count += 1
print(count)


# accessing the item ---------------------------------


employee = {'khairul' : 12000000, 'beex' : 900000}
print(employee['beex'])

fees = {'kd' : 2000, 'bx' : 30000}
fees['bx'] = 1000
print(fees)
fees['kd'] = fees['kd'] - (fees['kd'] * 20 / 100)
print(fees)


# Dictionary method ---------------------------

phone = {'name' : 'samsung', 'price' : 225000, 'model' : 's24 Ultra'}

print(phone.get('model', 'not found')) # key name , default value

phone['model'] = 's25 Ultra'
print(phone)

phone.pop('price')
print(phone)

phone.popitem()
print(phone)

del phone['name']
print(phone)

phone.clear()
print(phone)

phone.update({'name' : 'redmi'})
print(phone)

Phone = {}
n = int(input("how many phone : "))
for i in range(n):
    name = input("enter name : ")
    price = int(input(f"enter price of {name} : "))
    if name not in Phone:
        Phone[name] = price
    else:
        print("already exist...!")
print(Phone)

new_phone = phone.copy()
print(new_phone) 