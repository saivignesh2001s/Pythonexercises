'''
Tuple won't allow you to append,remove or update..so it is always make deep copy
if it is without immutable elements.
But with mutable elements,it makes shallow copy for inner complex elements if used copy.copy() or .copy() or slicing
To create deep copy,use copy.deepcopy()
'''
#import copy
tuple_1=[1,2,'ram',['want','paint']]
#tuple_2=tuple_1
#tuple_2=tuple_1.copy() throws error
#tuple_2=copy.copy(tuple_1)
#tuple_2=copy.deepcopy(tuple_1)
tuple_2=tuple_1[0:4:1]
print("Tuple 1 is",tuple_1)
print("Tuple_2 is",tuple_2)
tuple_1[3].append('arrogant')
print("After adding elements in tuple_1 inner list tuple_1 is",tuple_1)
print("After adding elements in tuple_1 inner list tuple_2 is",tuple_2)
