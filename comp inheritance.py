class Competition:
     def __init__(self,name,amount):
         self.__name=name
         self.__amount=amount
     def get_sprint(self):
         return self.__name
     def get_prize(self):
         self.__amount=self.__amount+(0.1*self.__amount)
     def get_amount(self):
         return self.__amount
class Cycling(Competition):
    def __init__(self,name,amount,country):
        super().__init__(name,amount)
        self.__country=country
    def getcountry(self):
        return self.__country
class shooting(Competition):
    def __init__(self,name,amount):
        super().__init__(name,amount)
class Shooting():
    def __init__(self,name):
        self.first=name
shoo=shooting('rifle',900)
print(shoo.get_sprint(),shoo.get_amount())
print(issubclass(shooting,Competition))
print(issubclass(Shooting,Competition))
c=Competition('100px',800)
p=c.get_sprint()
c.get_prize()
p1=c.get_amount()
print(p,p1)
cyc=Cycling('100px',900,'USA')
print(cyc.getcountry())
print(cyc.get_sprint(),cyc.get_amount())
print(issubclass(Cycling,Competition))
