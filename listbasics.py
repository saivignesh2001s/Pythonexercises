list1=['sai','rsm','prem']
print(list1)
print(type(list1))
print(list1[0])
print(list1[-1])
list1[1]='ram'
list1.append(5)
print('After appended the list',list1)
#list2=['ss','ps']
list1.extend(['ss','ps','ds'])
print('After extended the list',list1)
list1.insert(3,'pos')
print('After inserted list at 3rd pos: ',list1)
k=list1.index(5)
list1.remove(list1[k])
list.sort(list1)
print('Sorted list is: ',list1)
print('Example of shallow copy')
gate=list1
print('The gate list is',gate)
list1[2]='Premkumar'
print('The list1 is',list1)
print('The list1 is',gate)
print('Example of Deepcopy')
import copy
deep_copy=copy.deepcopy(list1)
print('The deep copy is',deep_copy)
list1[2]='Prem'
print('The list1 is',list1)
print('The deep copy is',deep_copy)
print('concatenating lists')
conca=['sad','happy']
list2=list1+conca
print('concatenated lists of list1 and conca is',list2)
print('popping the last element')
print('List 1 before being popped is',list1)
list1.pop()
print('List 1 after being popped is',list1)
print('Printing the list1 in reverse')
list1.reverse()
print(list1)
print('Finding the length of the list')
print('Length of the list1 is',len(list1))
print('Using the * operator with list')
list3=list1*3
print('The list 3 is',list3)
print('Sorted the list')
list4=sorted(list1)
print('After sorting the list',list4)


