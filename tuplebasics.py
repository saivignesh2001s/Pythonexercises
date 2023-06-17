int_tuple=(1,3,4)
#When i am trying for updating the item in a tuple it throws me an error
#int_tuple[1]=2
#print(int_tuple)
#When i am trying for removing the item in a tuple,it throws me an error
#int_tuple.remove(3)
#print(int_tuple)
#Tuple is immutable so you can't do this function
'''
Suppose you have a list in a tuple,you can modify that list
Except for it is immutable,every other including slicing,step size works same for the tuple too
'''
int_tp1=(1,2,4,[3,5,6])
print(int_tp1)
int_tp1[3][0]=4
print(int_tp1)
int_tp1[3].append(9)
print(int_tp1)
print(int_tp1*3,' printed the tuple 3 times')

tuple_a=(7,8,9,10,11,12,13)
tuple_b=('q','w','e','r','t','y')
result=zip(tuple_a,tuple_b)
print('zipped result is ',result)
'''dd=dict(result)
print('dictionary of zipped result is ',dd)'''
tuple_c,tuple_d=zip(*result)
print(tuple_c,tuple_d)
