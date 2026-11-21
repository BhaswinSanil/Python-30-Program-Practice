def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

n=int(input("Enter a number to find factorial of: "))
print(fact(n))