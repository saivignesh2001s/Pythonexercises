'''
inheritance-one class based out of another
            makes code reusability better.
            construct looks elegant in both functional and obj
            effectively utilise polymorphism
subclasses-child class of parent class
  is a relationship
class shape:
      pass
class shape():
      pass
class shape(Object):
      pass

Base class: The class which is used to derive other classes are called Base classes(Parent or super class)
Derived classes:The class which is being derived is called derived classes

Required instantiating arguments of super class also needed to instantiate the sub class also

first subclass


'''
import math
class shape:
      def __init__(self,shape_type,color="Red"):
          self.__type=shape_type
          self.__color=color
      def get_type(self):
          return self.__type
      def get_color(self):
            return self.__color
      def get_area(self):
            pass
      def get_perimeter(self):
            pass
class circle(shape):
      def __init__(self,radius,color="Green"):
            shape.__init__(self,'circle',color)
            self.__radius=radius
      def get_area(self):
            return math.pi*self.__radius*self.__radius
      def get_perimeter(self):
            return 2*math.pi*self.__radius
class square(shape):
      def __init__(self,side):
            shape.__init__(self,'square')
            self.__side=side
      def get_area(self):
            return self.__side**2
      def get_perimeter(self):
            return self.__side*4
c1=circle(1)
s2=square(4)
print(s2.get_area(),s2.get_perimeter())
print(c1.get_type(),s2.get_type())
print(c1.get_color(),s2.get_color())
s=shape("circle")
s1=shape("rectangle",color="Blue")
p=s.get_type()
print(type(s))
print(p)
m=s.get_color()
m1=s1.get_type()
print(m1)
m2=s1.get_color()
print(m2)
print(f"The name of the shape is {p} and the color of the shape is {m}")
print(f"The name of the shape is {m1} and the color of the shape is {m2}")

num=[40,70,20,80]
k=[i-20 if i>20 else "null" for i in num]
print(k)

k1=input("enter a string")
b=k1[0]
count=1
k2=""
for i in range(1,len(k1)):
    if(k1[i]==b):
          count=count+1
    else:
      k2+=b+str(count)
      b=k1[i]
      count=1
    if(i==len(k1)-1):
         k2+=b+str(count)
print(k2)
dict1={}
k3=""
for i in k1:
      if i in dict1:
            print(i,dict1[i])
            dict1[i]=dict1[i]+1
      else:
            dict1[i]=1
for i,j in dict1.items():
      k3+=i+str(j)
print(k3)


'''
Invoking Base class methods from sub classes

Super class and sub class hierarchies
'''
c3=circle(2)
area=c3.get_area()
peri=c3.get_perimeter()
print(area,peri)
help(shape)
print(shape.__dict__)
help(circle)

