class student:
    def __init__(self,name,gpa):
        self.__name=name
        self.__gpa=gpa
        self.__clubs=set()
        self.__Isactive=True
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def set_gpa(self,gpa):
        self.__gpa=gpa
    def get_gpa(self):
        return self.__gpa
    def get_clubs(self):
        return self.__clubs
    def set_clubs(self,club):
         self.__clubs.add(club)
    def remove_clubs(self,club):
        self.__clubs.remove(club)
    def get_Isactive(self):
        return self.__Isactive
    def set_Isactive(self,Isactive):
        self.__Isactive=Isactive
    def printdetails(self):
        print("I am {0} my cgpa is {1} my interests are in {2} I am {3}".format(self.get_name(),self.get_gpa(),self.get_clubs(),self.get_Isactive()))

d=[]
s1=student("sai",9.9)
s2=student("RandyPrasath",10.0)
s1.set_clubs('YRC')
s2.set_clubs('NCC')
s2.set_Isactive(False)
d.extend([s1,s2])
for i in d:
    print(i.get_name())
    print(i.get_gpa())
    print(i.get_clubs())
    print(i.get_Isactive())

print("---------------------------Parsing from  dictionary-------------------")

student_dict=[{"name":"sai","gpa":3.9,"clubs":["Football"]},
              {"name":"Lily","gpa":3.8,"clubs":["tennis"],"active":False},
              {"name":"Michael","gpa":3.7,"clubs":["tennis"]},
              {"name":"Joe","gpa":3.9,"clubs":["football"],"active":True}]
student1=[]
for i in student_dict:
    s=student(i["name"],i["gpa"])
    for i1 in i["clubs"]:
        s.set_clubs(i1)
    if("active" not in i.keys()):
        student1.append(s)
        continue
    else:
        s.set_Isactive=i["active"]
        student1.append(s)
    
for i in student1:
    i.printdetails()

    '''other way is th=o check for the key in dictionary and adding it'''

class circle:
     def __init__(self):
         self.__radius=0
     def get_radius(self):
        return self.__radius
     def set_radius(self,radius):
        self.__radius=radius
     def area(self):
        return 3.14*(self.__radius**2)
     def perimeter(self):
        return 3.14*2*self.__radius
     
s=circle()
i=int(input("Enter a radius"))
s.set_radius(i)
p=s.area()
print("area is"+" ",p)
k=s.perimeter()
print("perimeter is"+" ",k)
