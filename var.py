
# memeory allocation ------------------


a =  100
print("a", id(a))
b = 200
print("B", id(b))


# Creating myltiple variable in one line ----------------


name, age, salary = "khairul", 20, 2034
print(name), print(age), print(salary)


# assign single value to multiple variables --------------------------


num = age = value = 20
print(num), print(age), print(value)


# variable anotations -----------------------------------


name:str = 'khairul'
print(name)
name = 23
print(name)

# how to get list of keywords ----------------

import keyword
print("Keywords are : ", keyword)