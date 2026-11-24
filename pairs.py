lst=[]
n=int(input("Enter the size of list: "))
for i in range(n):
    e=int(input(f"Enter element at index{i}: "))
    lst.append(e)
target=int(input("Enter the target: "))
print("pairs adding upto target: ")
for i in range(n):
    for j in range(i+1,n):
        if lst[i]+lst[j]==target:
            print(lst[i],lst[j])