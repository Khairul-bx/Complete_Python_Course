
# creating set --------------------------------

s = {10, 20, 30}
print(type(s))
print(s)
x = set["2", 101, 102]
print(x)


# set method -----------------------------------


s = {'hello', 'world'}

s.add('beex')
print(s)
s.update(['uk', 'khairul'])
print(s)
s.remove('hello')
print(s)
s.discard('world')
print(s)
s.pop()
print(s)
s.clear()
print(s)
del s
print(s)


# set operation -------------------------------


s1 = {10, 20, 30, 40}
s2 = {20, 40, 50, 60}
print(s1 | s2)
union = s1.union(s2)
print(union)

print(s1 & s2)
new_set = s1.intersection(s2)
print(new_set)

print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
print(s1.difference(s2))

print(s1 > s2)
print(s1 < s2)
print(s1 == s2)

fs = frozenset([1,2,3])
print(fs)