'''
assignment operator,slicing produces fully shallow
copy.copy(),.copy() produces shallow when contain mutable elements
.deepcopy() produces deepcopy
'''

dict1={"Sam":40,"Gana":50}
#dict2=dict1

import copy
#dict2=dict1.copy()
#dict2=copy.copy(dict1)
#dict2=copy.deepcopy(dict1)
#dict2["Rama"]=90
#print(dict1,' ',dict2)

dict6={"Sam":50,"Gana":[90,120,190]}
#dict7=dict6

import copy
#dict7=dict6.copy()
#dict7=copy.copy(dict6)
dict7=copy.deepcopy(dict6)
dict6["Gana"].append(90)
print(dict6,' ',dict7)
