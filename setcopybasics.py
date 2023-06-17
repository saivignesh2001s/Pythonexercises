'''
set
assignment operator shallow
all other deep as no mutable elements are allowed
'''
k1=set([90,99,200,78])
#k2=k1
#k2=k1.copy()
import copy
#k2=copy.copy(k1)
k2=copy.deepcopy(k1)

k1.add(908)
print(k1,' ',k2)
