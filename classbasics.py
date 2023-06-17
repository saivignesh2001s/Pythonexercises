class student:
    pass
ob1=student()
ob1.name="sai"
ob1.email="xyz@gmail.com"
ob2=student()
ob2.name="sai22"
ob2.email="xyz22@gmail.com"
print(ob1.name,' ',ob1.email)
print(ob2.name,' ',ob2.email)
#you cannot access which are not declared

class student1:
    name=' '
    score=0
    active=True
    def __init__(self):
        print("Instance initiated")
    def --
list1=[]
obj1=student1()
obj1.name='Sai vignesh'
obj1.score=100
list1.append(obj1)
obj2=student1()
obj2.name='Vikram'
obj2.score=190
obj2.active=False
list1.append(obj2)


for x in list1:
    if(x.active==True):
       print(x.name+' is a current student with the score of',x.score)
    else:
        print(x.name+' is not a current student with the score of',x.score)
list2=[x.name for x in list1 if x.active==True]

print(list2)
