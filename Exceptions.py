#print(variable) Name error
try:
    print(variable)
except:
    print("Exceptiion occured(Name error),because 'variable' was not defined")

try:
    print(variable)
except NameError:
    print("Variable is not defined")
except:
    print("An unknown error occured")

#first except block which matches it will execute
#try except 
try:
    f=open("vv.csv")
except FileNotFoundError:
    print("No such file")
except:
    print("An unknown error occured")
while True:
    try:
        inputvar=int(input("please enter the number"))
        break
    except ValueError:
        print("Oops not a valid number.Try again")
#defining custom try except
attempts=0
while True:
    try:
        inputvar=input("please enter the number")
        inputvar=int(inputvar)
        break
    except ValueError:
        attempts+=1
        if(attempts<3):
            print("Oops not a valid number.Try again")
        else:
            print("You really want to enter a string")
            inputvar=str(inputvar)
            break
#Exception Hierarchy
try:
    f=open("cs.csv")
except OSError:
    print("Os error occured")
except FileNotFoundError:
    print("No such file")
try:
    f=open("cs.csv")
except FileNotFoundError:
    print("No such file")
except OSError:
    print("Os error occured")
finally:
    print("try except has ended")
try:
    a=int(5)
    b=str('Hekko')
    d=a+b+c
    print(d)
except TypeError:
     print("TypeError Found")
except NameError:
     print("NameError Found")
except ValueError:
     print("ValueError Found")
except e:
     print(e)
number=int(input("Enter a number"))
try:
    if(number>5):
        raise Exception("The number should not exceed 5.The value of number is {0}".format(number))
except Exception as e:
        print("Caught this error",repr(e))
    
import time
try:
    time.sleep(111)
except KeyboardInterrupt:
    print("KeyBoard Interrupt has occured")
#Chaining except blocks
'''
try:
    file=open()
    file.write()
except:
    print("something went wrong")
else:
    print("Nothing went wrong")
'''

    


