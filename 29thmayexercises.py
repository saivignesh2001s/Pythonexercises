#while loop=>save square numbers in dictionary
i=1
dict1={}
k=int(input("Enter a number till you want to store the num and square in the dictionary"))
while(i<=k):
     dict1[i]=i*i
     i=i+1
print("Num and its square in the dictionary is ",dict1)

#for loop=>add cube numbers in the list
list1=[]
k1=int(input("Enter a number till you want to cube from 1"))
for i in range(1,k1+1):
    g=i*i*i
    list1.append(g)
print("Cube numbers in the list ",list1)

#using continue print only prime numbers using continue,break and using parameterised and functions
def prime(a):
    if(a>1):
      for i in range(2,a):
          if(a%i==0):
             return False
             break
      else:
          return True
    else:
        return False
        
i=1
kp=int(input("Till what you want to get prime numbers"))
while i<kp:
      if(prime(i)):
         print(i)
         i+=1
         continue
      i+=1

      
#Checking for armstrong number in the range
def armstr(num):
    k=len(str(num))
    temp=num
    sum1=0
    while temp>0:
          k1=temp%10
          sum1+=k1**k
          temp=temp//10
    if(sum1==num):
        return True
    else:
        return False

ip=int(input("Enter armstrong number"))
if ip is True:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

#arbitrary function
def armstrongnum(*numbers):
    listk=[]
    for i in numbers:
        if(armstr(i)):
           listk.append(i)
    print("Armstrong numbers among them {0} is {1}".format(numbers,listk))
armstrongnum(123,14,153,167)


def fibo(p1):
     if(p1<=0):
         return 0
     elif(p1==1):
         return 1
     else:
         return fibo(p1-1)+fibo(p1-2)

print("\nFibonacci seq using recursive function")
po=int(input("Number of fibonacci sequence you want to print :"))
for i in range(0,po):
    k=fibo(i)
    print(k,end=" ")


print("\nLeft lower triangle abcde slope")
pok=int(input("enter number of rows you want to print"))
for i in range(pok):
    for x in range(65,65+i,1):
        print(chr(x),end=" ")
    print("")

print("\nupper triangle printing abcde")
for i in range(pok,0,-1):
     for x in range(65,65+i,1):
         print(chr(x),end=" ")
     print(" ")


print("\nTriangle printing from left side")
for k in range(pok):
    z=65
    for t in range(1,pok+1):
        if(t<pok-k):
             print(" ",end=" ")
        else:
            print(chr(z),end=" ")
            z=z+1
    print(" ")

#Functions using default key word
print("\nExample for default keyword")
def cname(name,age=18):
     print("I am {0} and am {1}".format(name,age))
cname('Sai',19)
cname('Ambika')
cname(age=22,name='Saii')

#If..elif..else..Nested else
print("\nFinding the given year is leap year or not")
kpl=int(input("Enter a year to find it is leap year or not"))
if(kpl%4==0):
     if(kpl%100!=0):
          print("It is leap year")
     elif(kpl%400==0):
          print("It is leap year")
     else:
          print("It is not leap year")
else:
     print("It is not leap year")


#Lambda function
print("\n Lambda function")
ab=int(input("Enter a number to square"))
c=lambda a:a**2
print("\nSquare of given number is ",c(ab))

#while..else
ping=int(input("Type a multiplication table"))
i=1
while(i<=10):
     print(i,' ','*',ping,'=',i*ping)
     i+=1
else:
     print("That's it")


#some inbuilt functions
print("\nSome inbuilt functions")
import math
print("Sqrt of 7 is ",math.sqrt(7))
print("ceil of 7.999 is ",math.ceil(7.999))
print("floor of 7.999 is ",math.floor(7.999))
print("fabs of -90 is ",math.fabs(-90))
print("2 power 3 is ",math.pow(2,3))
