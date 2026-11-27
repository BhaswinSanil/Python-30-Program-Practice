lt=[1,2,2,3,4,4,5,5,5,6]
unique=list(set(lt))#not ordered
unique2=list(dict.fromkeys(lt))#ordered
print(unique)
print(unique2)