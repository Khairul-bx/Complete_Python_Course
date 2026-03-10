

# create tuple ----------------------------


tp = (1, 2, 3)
print(type(tp))
print(tp)
data = ['khairul', 1.78, 10]
print(tuple(data))


# unpacking tuple --------------------------


data = (1052, "Khairul", "Dhaka", 2026)
roll, name, address, batch = data
print(f"name is: {name}\nRoll is : {roll}\nAddress : {address}\nBatch : {batch} ")


personal = ('khairul', 'Dhaka', True)
academic = (100, 90, 'A', 'Pass')
detail = personal + academic
print(detail)
print(type(detail))

del data
print(data)


# Membership in  tuple ------------------------


personal = ('khairul', 'Dhaka', True)
print('Dhaka' in personal)

index = 0
while index < 3:
    print(personal[index])
    index += 1


# indexing and slicing --------------------------


t = (20, 30, 'khairul')
print(t[0])
print(t[-1])
print(t[1:2:1])

# tuple unpacking -------------------------

t = 1, 2, 3
a, b, c = t
print(a, b, c)
a, *b, c = (1, 2, 3, 4, 5, 6)
print(a, tuple(b), c)


# tuple method --------------------------------


data = (20, 10, 30, 40, 50, 40, 30, 40, 50)
print(data.index(40, 5, -2)) # item -> start -> end
print(data.count(40))


# build in function -----------------------------


t = (5,2,8,1)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

import sys
print(sys.getsizeof((1,2,3)))
print(sys.getsizeof([1,2,3]))

print(all(t))
print(any(t))
print(sorted(t))

tup = (20, 30, [40, 50, 60])
print(tup)
print(id(tup))
tup[-1][0] = 100
print(tup)