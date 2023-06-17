'''You can't add mutable data types inside the set'''
#k2={1,2,3,(4,5,6),[7,8,9]} This is not possible in set
k2={1,2,3,(4,5,6)}

print('My set is',k2)
print('Length of my set is',len(k2))
#discard and remove diff is that when we give non existing names inside discard it won't throw error but in remove it does
k2.discard(3)
print("First discarding ",k2)
k2.discard(3)
print("Second discarding ",k2)
#k2.remove(3)=>Throws error 
#print("Now trying to remove again ",k2)
'''
To clear,.clear()'''
k2.clear()
print("After clearing k2", k2)
print("\n")
#For strings,max and min see the dictionary order which comes fast(min) and last(max)..supported in same sety of data types only
string_set1={'Ramesh','Kamesh','Varathan'}
string_set2={'Rajesh','Ramesh'}
string_set3={'Ravi','Varathan'}

print("My string_set1 is ",string_set1)
print('Max of my set is',max(string_set1))
print('Min of my set is',min(string_set1))
#Now doing some set operations
print("\n")
print("Printing all my three sets ",string_set1,' ',string_set2,' ',string_set3)
print("Union of first two sets",string_set1.union(string_set2))
print("Union of all the three sets",string_set1.union(string_set2,string_set3))
print("Intersection of first two sets",string_set1.intersection(string_set2))
print("Intersection of all three sets",string_set1.intersection(string_set2,string_set3))
print("Difference of first two sets",string_set1.difference(string_set2))
print("Difference of first one with other two",string_set1.difference(string_set2,string_set3))
print("Difference A/(B/C)",string_set1.difference(string_set2.difference(string_set3)))
#You have unionupdate,intersectionupdate and difference update to update the values of respective functions in the first set
print("\n")
print("Disjoint,subset and superset")
print("{10,20,30} is disjoint of {40,50,60}",{10,20,30}.isdisjoint({40,50,60}))
print("{10,20,40} is disjoint of {40,50,60}",{10,20,40}.isdisjoint({40,50,60}))

print("\n")
print("{10,20} is a subset of {10,20,30}",{10,20}.issubset({10,20,30}))
print("{10,20,40} is a subset of {10,20,30}",{10,20,40}.issubset({10,20,30}))

print("\n")
print("{10,20,30} is a superset of {10,20}",{10,20,30}.issuperset({10,20}))
print("{10,20,40} is a superset of {10,20,30}",{10,20,40}.issuperset({10,20,30}))




print("\n")
'''declare a set and get and print the elements'''
z=int(input("Number of elements you want in set"))
k1=set()
for i in range(0,z): 
    d=int(input('Get element'))
    k1.add(d)
print(k1)
#print(k1[0]) will throw error as set do not have a look up
