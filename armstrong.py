start=int(input("Enter the starting range: "))
end=int(input("Enter the ending range: "))

for num in range(start,end+1):
    digits=str(num)
    power=len(digits)

    total=0
    for d in digits:
        total+=int(d)**power

    if total==num:
        print(num)