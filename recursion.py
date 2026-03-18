


def demo():
    print("hello")
    demo()
demo()

n = int(input("enter the value of n : "))
def natural(n):
    print(n)
    if n == 0:
        return
    return natural(n-1)
natural(10)