
'''
Shallow copy->Assignment operator
Shallow copy if with complex elements inside->copy.copy(),.copy()
Deep copy->copy.deepcopy(),slicing
'''
list1=[10,20,30,40,50,60]
list1.remove(60)
print("Trying using assignment operator")
list2=list1
print("List1 is ",list1)
print("List2 is ",list2)
list2[0]=90
print("List1 after changing first element in list2",list1)
print("List2 after changing first element in list2",list2)

print("\n Trying using copy.copy operator")
import copy
list3=[10,20,30,[40,50,60]]
list4=copy.copy(list3)
print("List3 is ",list3)
print("List4 is ",list4)
print("First trying to modify in outer list")
list3.append(99)
print("List3 after appending element in outer list in list3 is",list3)
print("List4 after appending element in outer list in list3 is",list4)
print("Fine..It is not reflecting.Let us check for inner list")
list4[3].remove(60)
print("List3 after popping element in inner list in list4 is",list3)
print("List4 after popping element in inner list in list4 is",list4)

print("\n Trying using .copy() operator")
import copy
list5=['Amar','Shyam','thyagam',['Naga','Nanna','Nange']]
list6=list5.copy()
print("List5 is ",list5)
print("List6 is ",list6)
print("First trying to modify in outer list")
list5.append('Samantha')
print("List5 after appending element in outer list in list5 is",list5)
print("List6 after appending element in outer list in list5 is",list6)
print("Fine..It is not reflecting.Let us check for inner list")
list6[3].remove('Naga')
print("List7 after popping element in inner list in list6 is",list5)
print("List8 after popping element in inner list in list6 is",list6)


print("\n Trying using .deepcopy()and slicing operator")
import copy
list7=['Amar','Shyam','thyagam',{'Mani':80,'Kani':90}]
list8=copy.deepcopy(list7)
#list8=list7[:]
print("List7 is ",list7)
print("List8 is ",list8)
print("First trying to modify in outer list")
list7.append('Samantha')
print("List7 after appending element in outer list in list7 is",list7)
print("List8 after appending element in outer list in list7 is",list8)
print("Fine..It is not reflecting.Let us check for inner list")
list8[3].pop('Mani')
print("List5 after popping element in inner list in list8 is",list7)
print("List6 after popping element in inner list in list8 is",list8)





