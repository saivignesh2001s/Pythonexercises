student_details={"Sai":2018,
                 "Prem":2019,
                 "Sathya":[2020,2021]}
student_details["Venkatesh"]=2023
print(student_details)
print(student_details.keys())
print(student_details.values())
print(student_details.items())
dt1=student_details.copy()
dt1["Venkatesh"]=2021
student_details["Sathya"][1]=2022
print("student details",student_details)
print("dt1",dt1)
print(student_details.get("Sai"))
student_details["Shankar"]=2021
print(student_details)
student_details['Sathya']=2021
print(student_details)
k="Sathyam" in student_details.keys()
print(k)
k1=2019 in student_details.values()
print(k1)

print("Number of records in student_details",len(student_details))
print("Number of keys in student_details",len(student_details.keys()))
print("Number of values in student_details",len(student_details.values()))
print("Lexicographically order sort",sorted(student_details))
print("Lexicographically reverse order sort",sorted(student_details,reverse=True))
print("Records in list of tuples",student_details.items())
import copy
student_details1=copy.deepcopy(student_details)
student_details1.pop("Sathya")
print("student_details1",student_details1)
print("student_details",student_details)

student_details_copy=student_details#Shallow copy
dooze=student_details_copy.pop("Sathya")
print("The value of the popped tuple is",dooze)
print(student_details_copy)
print(student_details)
student_details_copy.popitem()
print(student_details_copy)
print(student_details)
stud_details={"Shankar":2024,"Samantha":2023}
student_details.update(stud_details)
print("Updated student details",student_details)

print(any([]))



fruit_qty={}
kz=int(input("Enter a number of fruits you want to enter"))
for x in range(0,kz):
     g=input("Enter a fruit name")
     fruit_qty[g]=int(input("Fruit quantity consumed"))

print(fruit_qty)

fruit_qty1={
    "Banana":[23,45,67,99],
    "Apple":[78,98,99,100],
    "Orange":[34,45,67,89]}
print(fruit_qty1["Banana"])
print(fruit_qty1["Banana"][1])
fruit_qty1["Banana"][1]=90
print(fruit_qty1["Banana"][1])


fruit_qty2={
    "Banana":{"Sun":67,"Fri":76,"Sat":98},
     "Apple":{"Sun":65,"Fri":75,"Sat":100},
     "Mango":{"Sun":70,"Fri":80,"Sat":90}
    }
print(fruit_qty2["Banana"])
print(fruit_qty2["Banana"]["Sun"])
fruit_qty2["Banana"]["Sun"]=98
print(fruit_qty2["Banana"]["Sun"])






