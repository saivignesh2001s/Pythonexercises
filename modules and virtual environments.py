#inbuilt module
#custom module
#virtualenv tool
#module =>group of functions and also class definitions

'''
import os
print(os.getcwd())#current working directory
print(os.getcwd.__doc__)#return a unicode string representing the current working dirctory
'''
'''
from os import getcwd
print(getcwd())
os.mkdir("tempdir")#it throws error it has import os
os.listdir("tempdir")#listing the directories
'''
'''
import math as m
print(m.sqrt(49))
'''
#commonly used python modules
import sys #command line argument
print(sys.path)
import time
from time import asctime
print(asctime())
help(time)#man page of the module
import datetime #object oriented type
print(datetime.datetime.now())
import random #random generator
print(random.__file__)#random source file located
print(random.random())#floating point
print(random.rsndint(1,10)#both upper or lower bound included
#custom module
#create function file
#to make it that distributable package
#use setup tools
'''
from setuptools import setup
setup{
    name="calculatorcustom",
    version=1.0,
    description="my python module",
    author="",
    authoremail="",
    url="",
    py_modules=["calcu;ator"]}
'''
#python setup.py sdist distributable file in parent directory
#warning read me file
#archive file created is distributable package
#calculator-1.0 tar.gz

'''
Installing and using custom module
pip install calculator-1.0.tar.gz
help('modules') #list of available modules

'''
#configuring virtual environments
'''
virtualenv for isolated python environments
ls -n
list the files there
four files one python2 script syntax files,python2 and 3 file,shellscript(sqlalchemy)
isolated pyhton environment
pip install virtualenv --upgrade
virtualenv first_env
cd in this
bin include lib
which python2(where python2)
which python3
virtualenv -p python2 path

Activating virtualenv
virtualenv --secondenv
source activate path of first path
pip list
deactivate

configuring virtual env
chmod +x
SQL AlChemy version


'''
'''
import numpy as np #array optimised #less space than lists and linear algebraic expressions
array1=np.array([['a','b'],['c','d']])
print(array1)

