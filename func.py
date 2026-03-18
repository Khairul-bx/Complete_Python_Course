
# Function creation --------------------------------------


def addition(a, b):
    print("Welcome")
    print("Addition is : ", a + b)
addition(10, 20)

def display():
    print("welcome")
display()
print("-" * 50)


# scope --------------------------------------


def my_func():
    x = 10  # Local variable
    print(x)
my_func() 

def outer():
    y = 20
    def inner():
        print(y)  # Enclosing variable
    inner()
outer() 

z = 30  # Global variable
def my_func():
    print(z)  # Access global variable
my_func()  

a = 5
def update():
    global a
    a = 10
update()
print(a)

print(len("hello"))  # print() and len() are built-in


# return statement ------------------------------------------------


def simpl_interest(p,n,r):
    si = (p*n*r)/100
    print("Simple interest is : ", si)
    return si
P = 10000
N = 9
R = 9.25
simpl_interest(P,N,R)


# Type of argument --------------------------------------------------


def add(a, b):
    print(a + b)
add(2, 3) # order -> value pass

def info(name, age):
    print(name, age)
info(age=20, name="Rahim") # variable name -> value pass

def greet(name="Guest"):
    print("Hello", name)
greet()        # Hello Guest
greet("Ali")   # Hello Ali

def total(*numbers):
    print(sum(numbers))
total(1, 2, 3)        # 6
total(5, 10, 15, 20)  # unlimited positional argument can take

def details(**data):
    print(data)
details(name="Rahim", age=20) # unlimited keyword argument can take

def func(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)
func(1, 2, 3, 4, x=100, y=200) # positional -> Deafault -> *args -> **kwargs


# Lambda Function ------------------------------------------------------


add = lambda x,y : x + y
print(add(10,20))

num1 = 10
num2 = 20
max1 = lambda n1, n2: n1 if n1 > n2 else n2
max(num1, num2)

result = (lambda num : num + 1)(int(input("enter the number : ")))
print(result)


# Filter Function -------------------------------------------------------


data = [23, 22, 45, 66]
filter_obj = filter(lambda num : num % 2 == 0 , data)
print(filter_obj)

nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

names = ["Rahim", "Karim", "Ali", "Rafi"]
result = list(filter(lambda name: len(name) > 4, names))
print(result)

data = [0, 1, "", "hello", None, 5]
result = list(filter(bool, data))
print(result)


# Map Function -------------------------------------------------------


nums = [1, 2, 3, 4]
def square(x):
    return x * x
result = list(map(square, nums))
print(result)

a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)

names = ["rahim", "karim", "ali"]
result = list(map(lambda name: name.upper(), names))
print(result)


# Reduce Function ---------------------------------------------------


from functools import reduce
nums = [1, 2, 3, 4, 5]
def add(x, y):
    return x + y
result = reduce(add, nums)
print(result)

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(result)

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)

nums = [5, 8, 2, 9, 3]
max_num = reduce(lambda a, b: a if a > b else b, nums)
print(max_num)

nums = [1, 2, 3, 4, 5, 6]
result = reduce(
    lambda x, y: x + y,
    map(lambda n: n**2, filter(lambda n: n % 2 == 0, nums))
)
print(result)


# Partial Function --------------------------------------------------


from functools import partial
def power(base, exp):
    return base ** exp
cube = partial(power, exp=3)  # exponent 3 fix
print(cube(2))  # 2^3
print(cube(5))  # 5^3

def greet(greeting, name):
    return f"{greeting}, {name}!"
say_hello = partial(greet, "Hello")
say_hi = partial(greet, "Hi")
print(say_hello("Ali"))
print(say_hi("Rahim"))

nums = [1, 2, 3, 4]
def multiply(x, factor):
    return x * factor
double = partial(multiply, factor=2)
result = list(map(double, nums))
print(result)