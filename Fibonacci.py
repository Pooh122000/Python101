# 0,1,1,2,3,5,8...
def fibonacci(f):
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(f):
        c = a+b
        print(c)
        a, b = b, c


fibonacci(8)
print("***********")
fibonacci(5)
print("***********")
fibonacci(4)
