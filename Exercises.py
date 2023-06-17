student_marks={
   "Jenny":92,
   "Harry":78,
   "Dimpy":56,
   "Rahul":41,
   "Aniket":99,
   "Prem":34
    }
student_grades={}
def assigngrades(student_marks):
    for i in student_marks:
        if(student_marks[i]>90 and (student_marks[i]<100)):
            student_grades[i]="A+"
        elif(student_marks[i]>80 and (student_marks[i]<90)):
             student_grades[i]="A"
        elif(student_marks[i]>70 and (student_marks[i]<80)):
             student_grades[i]="B+"
        elif(student_marks[i]>60 and (student_marks[i]<70)):
             student_grades[i]="B"
        elif(student_marks[i]>50 and (student_marks[i]<60)):
             student_grades[i]="C"
        elif(student_marks[i]>40 and (student_marks[i]<50)):
             student_grades[i]="D"
        else:
            student_grades[i]="F"
    return student_grades
k=assigngrades(student_marks)
print(k)

student_data=[
    {
        "Name":"Ram",
        "roll_no":10,
        "age":20,
        "course":"Python"
        },
    {
         "Name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"Java"
         }
    ]
def additem(dict1):
    student_data.append(dict1)

dict1={}
dict1["Name"]=input("Enter the name")
dict1["roll_no"]=int(input("Enter the roll_no"))
dict1["age"]=int(input("Enter the age"))
dict1["course"]=input("Enter the course name")
additem(dict1)
print(student_data)
