#Set Union
odd_num_1={1,3,5,7}
odd_num_2={7,9,11,13,17}

odd_num_1=odd_num_1.union(odd_num_2)
odd_num=odd_num_1|odd_num_2

print (odd_num_1)
print (odd_num)

#Set Intersection

inter_odd_num=odd_num_1.intersection(odd_num_2)
print (inter_odd_num)
inter_odd_num_1=odd_num_1 & odd_num_2

print (inter_odd_num_1)

#Set difference

even_num_1={2,4,6,8}
even_num_2={6,8,10,12}

even_num=even_num_1-even_num_2

even_num_1=even_num_1.difference(even_num_2)

print (even_num_1)
print (even_num)

#Symmetric difference(elements which are not common in both sets)Union minus intersection
sym_diff_1={2,4,6,8}
sym_diff_2={6,8,10,12}

sym_diff=sym_diff_1.symmetric_difference(sym_diff_2)
sym_diff_1=sym_diff_1^sym_diff_2
# sym_diff_1.symmetric_difference_update(sym_diff_2)#Updates set with symmetric diff
# print (sym_diff_1)

print(sym_diff_1)
print(sym_diff)



#To check if an element exists in a set

odd_num_1={1,3,5,7}
#returns a boolean value
print (3 in odd_num_1)

#deleting an entire set

del odd_num_1

#print (odd_num_1)