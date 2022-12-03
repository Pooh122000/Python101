# natural numbers

def num(n):
    sum = 0
    for i in range(n+1):
        sum = sum + (i*i)

    print("Sum: ", sum)


num(10)
