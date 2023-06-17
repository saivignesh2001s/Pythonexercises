#Get the string
k=input("Enter a string :")
k=k[0:5]#strip the string to 5 characters irrespective of its length
print("string k with 5 characters",k)
#If you want to assign each character of string to individual variable
a,b,c,d,e=k
print('The characters are',a,b,c,d,e)
#If you want to assign only the first two characters
a1,b1,_,_,_=k
print("a1,b1 are ",a1,' ',b1," respectively")
#or you can just access k[0],k[1]
print(k[0],' ',k[1],' are the first two characters')
#string is immutable so you can't update the element,remove or insert once declared
#k[0]='w'
#print("Trying to update element ",k)

#Using slicing,you can get substrings also
#negative indexing
print("Negative indexing ",k[-4:-1])

#indexing with step sizing
print("Reverse the elements ",k[-1:-6:-1])
'''
Check for palindrome
'''

if(k[0:len(k)]==k[len(k)-1:-6:-1]):
   print("It is palindrome")
else:
    print("It is not palindrome")

# del k =>memory association with the variable freed up and you can't access this element further

# Some invoking functions

'''
Check the string starts with S and ends with T"
'''
if(k.startswith('S') and k.endswith('t')):
    print("Yes it starts with S and ends with t")
else:
    print("No it is not starting with S and ending with t")


'''
Print the occurences of each character in a string
'''
print('The characters and corresponding occurences are: ')
list1=[]
for x in k:
    if x[0] not in list1:
       d=k.count(x[0])
       list1.append(x)
       print(x[0],' occurs ',d,' times')

'''
Printing the uppercase and lowercase
'''

print('The upper and lower of ',k,' is ',k.upper(),' ',k.lower(),' respectively')

'''
Index throws error for non existing character while find gives -1
'''
print('Example for find')
if k.find('e')!=-1:
    print('e is present')
else:
    print('e is not present')


print('\n')
print('Split the word New delhi using space')
p='New Delhi'
d=p.split(' ')
print('The split words are ',d)
print('Join the words')
d1=' '.join(d)
print('Joined words from ',d,' is ',d1)

    
