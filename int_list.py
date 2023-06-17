print('Integers with list')
int_list=[55,34,23,11,10]
print('Maximum number in the list is',max(int_list))
print('Minimum number in the list is',min(int_list))
print('Length of the given integer list is',len(int_list))
print('Sum of all elements given in the list is',sum(int_list))
print(all(int_list))
print(any(int_list))
print('Let us perform some slicing operations')
print('The elements from 2 to 4 is',int_list[2:5])
print('The elements from 0 to 2 using negative indexing',int_list[0:-3])
print('The elements from 0 to 5 in the step size of 2',int_list[::2])
print('The elements from 5 to 0 in the step size of 2(backwards)',int_list[-1:-6:-2])
print('slicing helps in creating deep copy')
int_list1=int_list[0:6]
print('The initial int_list1 is',int_list1)
int_list.append(55)
print('The int_list is',int_list)
print('The int_list1 is',int_list1)
print('set of the int_list is',set(int_list))
int_list[6:-1]=[99,88]
print('The new int_list is',int_list)
list_a=[1,2,3,4,5]
list_b=['a','b','c','d','e']
result=zip(list_a,list_b)
print('zipped result is',result)
#k=dict(result)
#print('zipped result in list',k)
list_c,list_d=zip(*result)
print('list-c is',list_c,'\nlist_d is',list_d)
print(all([-1,-1]))
print(int_list1[-2:-4])
lista=[2,3,4]
listb=lista
lista.clear()#When you clear it,memory contents of the element deleted
print(listb)
print(lista)
del lista
print(listb)
print(lista)#list stored in the memory released,so will throw error

