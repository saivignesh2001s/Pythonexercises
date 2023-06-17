
#If else
Income=int(input("Enter the income"))
Expenditure=int(input("Enter the expenditure"))
if(Expenditure>Income):
    print("No savings")
else:
    savings=Income-Expenditure
    print("My savings ",savings)

#Swapping without temporary variable
print("\n swap without temp variable in the list")
list1=["Samantha","Vanaja","Kandha"]
print(list1)
lok=input("Enter the names you want to swap with comma")
list2=lok.split(',')
i=list1.index(list2[0])
j=list1.index(list2[1])
list1[i],list1[j]=list1[j],list1[i]
print("Swapped list is ",list1)


#Splitting the list into two equal parts
list1=["Vanjam","Kantha","Radha"]
print("First half of the list is",list1[:len(list1)//2])
print("Second half of the list is",list1[len(list1)//2:])
