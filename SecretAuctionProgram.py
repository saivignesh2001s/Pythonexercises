import os
'''
l=[]
def additem(getname,getamount):
    dict1={}
    if(getname):
        dict1["name"]=getname
    if(getamount):
        dict1["amount"]=getamount
    l.append(dict1)
def findmax():
    dict1=l[0]
    for i in l:
        if(i["amount"]>dict1["amount"]):
            dict1=i
    return dict1
'''
bidder_det={}
def findmax():
    maxi=0
    winner=""
    for i in bidder_det:
        if bidder_det[i]>maxi:
           maxi=bidder_det[i]
           winner=i
    print(f'The winner of bid is {winner} and amount is {bidder_det[winner]}')
wannabe=False
while not wannabe:
    getname=input("What is your name\n")
    getamount=int(input("The amount you going to bid\n"))
    bidder_det[getname]=getamount
    k=input("Anymore bidders.Type yes to continue\n").lower()
    if(k!='yes'):
        g=findmax()
        wannabe=True
    else:
         os.system("clear")
         
'''other way with only dictionary'''
