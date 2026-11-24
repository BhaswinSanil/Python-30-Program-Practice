def counter(n):
    n=abs(n)
    if n==0:
        return 1
    count=0
    while n:
        count+=1
        n=n//10
    return count

def sum(n):
    sum=0
    n=abs(n)
    while n:
        sum+=n%10
        n=n//10
    return sum

n=int(input("Enter n: "))
print(f"Count: {counter(n)}, Sum: {sum(n)}")