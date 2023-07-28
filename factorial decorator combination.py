import copy
s=input("Enter a string")
def checkpositive(func):
    print(func)
    def wrapper(n):
        if(n>0):
            return func(n)
        else:
            raise ValueError
    return wrapper
@checkpositive        
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
limit=fact(len(s))
for i in range(limit):
    st=copy.deepcopy(s)
    temp=i
    sk=""
    for j in range(len(st),0,-1):
        rem=temp%j
        sk=sk+st[rem]
        st=st.replace(st[rem],"")
        temp=temp//j
    print(sk)
