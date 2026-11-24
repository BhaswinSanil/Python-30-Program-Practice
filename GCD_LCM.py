def gcd(a,b):
    a,b=abs(a),abs(b)
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    if a==0 or b==0:
        return 0
    return abs(a*b)//gcd(a,b)


if __name__ == "__main__":
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print(gcd(a,b))
    print(lcm(a,b))