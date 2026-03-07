
# while loop ------------------------------


count = 1
while count <= 3 :
    print("Inside loop")
    count += 1
    if count == 2:
        break
else:
    print("Inside else")


# nested while loop ------------------------

i = 1
while i <= 3:
    print("Outer loop")
    j = 1
    while j <= 3:
        print("Inner loop")
        j += 1
    i += 1


# range functionn ---------------------------


print(list(range(2, 10+1, 2)))


# for loop -----------------------------------


name = 'khairul'
for i in name:
    print(i)

for num in range(1, 10+1, 1):
    print(num)

l1 = [1, 20, 30, 4, 12]
for var in l1:
    print(var + 1)

digit = [0, 1, 5]
for x in digit:
    print(x)
    if x == 5:
        break
else:
    print("No items left")


# match case -------------------------------


status_code = 404
match status_code:
    case 200:
        print("Success")
    case 404:
        print("Page not found")
    case 500:
        print("Internal server error")
    case _:
        print("Invalid status code")
    

# Ternary operator ----------------------------


age = 20
msg = "You can vote" if (age >= 18) else "You can't vote"
print(msg)


# walrus operator -------------------------------


print(a := 100)

data = [10, 20, 30, 40]
i = -1
while (i := i+1) < (n := len(data)):
    print(data[i])
