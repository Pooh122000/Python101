name = input("Enter the sting: \n")

rev = name[::-1]
print(rev)

if name == rev:
    print("PALINDROME")

else:
    print("NOT PALINDROME")
