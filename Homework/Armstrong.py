def armstrong(n):
    total = 0
    a = n
    for i in range(len(str(n))):
        rem = int(a % 10)
        expo = rem ** (len(str(n)))
        total = total + expo
        a = int(a / 10)

    return total


print(armstrong(371))
print("*******************")
print(armstrong(370))
print("*******************")
print(armstrong(407))
print("*******************")
print(armstrong(8208))
print("*******************")
print(armstrong(1634))
print("*******************")
print(armstrong(54748))
