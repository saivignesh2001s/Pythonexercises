#List within a list is called nested list
k2=[[1,23,44],[45,66,77]]
print("Nested list is ",k2)
#You can access nested listed items
print("First item in the list", k2[0])
print("First element in the first item in the list",k2[0][0])
#Slicing possible for whole list also
print("Reversing the list",k2[-1::-1])
#slicing also possible
print("Reversing the first item in the list using slicing",k2[0][-1::-1])
#You can convert into tuple easily
k3=tuple(k2)
print("Lists in tuples is",k3)
#You can convert dictionary if the inside list contains only two elements


