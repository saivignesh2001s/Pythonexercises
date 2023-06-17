#strings always deep copy when assigning,.copy or in deep copy function

str1=input("Enter a string")

print("\nTrying using assignment operator")
str2=str1
print("Assigned str1 to str2"," str1 is ",str1," str2 is ",str2)
str1="Hello world"
print("Now modified str1")
print("After modified str1,str1 now",str1)
print("After modified str1,str2 now",str2)



print("\nTrying using copy.copy operator")
import copy
str3=input("Enter a string")


str4=copy.copy(str3)
print("Assigned str3 to str4"," str3 is ",str3," str4 is ",str4)
str4="Hello world"
print("Now modified str4")
print("After modified str4,str3 now",str3)
print("After modified str4,str4 now",str4)

print("\nTrying using copy.deepcopy operator")
import copy
str5=input("Enter a string")


str6=copy.deepcopy(str5)
print("Assigned str5 to str6"," str5 is ",str5," str6 is ",str6)
str5="Hello world"
print("Now modified str5")
print("After modified str5,str5 now",str5)
print("After modified str6,str6 now",str6)




