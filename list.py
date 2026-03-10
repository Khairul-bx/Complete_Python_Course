
# creating list -------------------------


data = [10, 20, 'heello', 30.4, 3+2j]
print(type(data))
print(data)


# indexing and slicing ----------------------


list1 = ['yes', 10, 20, 30]
print(list1[0])
print(list[-1])

list2 = [[1, 2, 3], "khairul", [4, 5, 6]]
print(list2[0][0])


# concatenation of list ---------------------------


l1 = [10, 20, 30, 'hello']
l2 = [40, 50, 60, 'hi']
print(l1 + l2)


# iteration through list -----------------------


l1 = [10, 20, 30]
l2 = [40, 50, 60]
for item in l2:
    print(item + 1)
print(l2)


# membership in list --------------------------


l1 = [10, 'hello']
print(10 in l1)
if 'hello' in l1:
    print("present")
else:
    print("not present")


# deletion of list ---------------------------


l1 = [10, 20, 30]
del l1
print(l1)


# length of list -----------------------


l1 = [10, 20, 30]
count = 0
for i in l1:
    count += 1
print(count)

name = ['khairul', 'upoma']
print(max(name, key=len))
print(min(name, key=len))


# finding maximum and minimum -----------------------


nums = [12, 34, 64, 24, 7, 2, 76, 73, 65, 33]
mx = nums[0]
mi = nums[0]
for ele in nums:
    if ele > mx:
        mx = ele
    if ele < mi:
        mi = ele
print(mx)
print(mi)


# adding item in list -----------------------------


l1 = []
l1.append('flower')
print(l1)
for i in range(3):
    name = input("enter name : ")
    l1.append(name)
print(l1)

l1.extend('100')
print(l1)

l1.insert(len(l1), 'boom')
print(l1)


# removing element -----------------------------------


cart = ['mobile', 'keyboard', 'mouse', 'laptop', 'mouse']
cart.remove('mouse')
print(cart)

cart.pop()
print(cart)
cart.pop(1)
print(cart)

del cart[0]
print(cart)

print(cart.clear())


# searching ------------------------------------------


li = [10, 20, 30, 8, 9]

print(li.index(10))
print(li.count(20))
li.sort()
print(li)
li.sort(reverse=True)
print(li)
li.sort(key=lambda x : x % 10)
print(li)


li.reverse()
print(li)

a = li.copy()
print(a + li)

a,b,*c = [1, 2, 3, 4, 5]
print(c)