numlist=[10,20,30,40]
def main():
     sum1=0
     count=0
     for i in numlist:
         count+=1
         sum1+=i
     print(count)
     print(sum1)
if __name__=="__main__":
    main()

#jupy notebooks lot of advantages
#python shell
#few lines py code..
#\033c
...
...
'''
import sys
sys.argv[0]
len(sys.argv)
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-display")
args=parser.parse_args()
print(args.display)

python scripts.py -display ""

import sys
number=1
if(len(sys.argv)==2):
     number=int(sys.argv[1])
for i in range(number):
     print("Hello World")
import sys
arg1=int(sys.argv[1])
arg2=int(sys.argv[2])
print(arg1+arg2)

rparse module
sys.rv
required or not
documentaion
import argparse
ap=argparse.ArgumentParser()
p.add_argument("-a","--first_operand",
required=True,
help=-"first operand")
p.add_argument("-b","--second_operand",
required=True,
help=-"second operand")
args=vars(ap.parse_args())
a=int(args[first operand])
b=int(args[second operand])
help usage info
'''
