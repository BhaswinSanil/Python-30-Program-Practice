a={1,2,3,4,5,6}
b={5,6,7,8,9,10}

union_op=a|b
union_meth=a.union(b)
print("Union (A|B): ",union_op)
print("union Method: ",union_meth)

inter_op=a&b
inter_meth=a.intersection(b)
print("intersection operator: ", inter_op)
print("intersection method: ",inter_meth)

diff_op=a-b
diff_meth=a.difference(b)
print("difference operator: ",diff_op)
print("difference method: ",diff_meth)

#Symmetric difference ele in a or b but not in both
sym_op=a^b
print("Symmetric difference: ",sym_op)
