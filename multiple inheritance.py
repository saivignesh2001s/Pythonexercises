class Father:
    def height(self):
        print("I inherited my height from father")
class Mother:
    def intelligence(self):
        print("I inherited my intelligence from mother")
class Child1(Father,Mother):
    def experience(self):
        print("I have 10 yrs")
class Child2(Mother,Father):
    def experience(self):
        print("I have 10 yrs")
help(Child2)
help(Child1)
c=Child1()
c.height()
c.intelligence()
c.experience()

class Employee:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        print(self.__name)
    def get_age(self):
        print(self.__age)
class Salary:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        print(self.__salary)
class Database(Employee,Salary):
    def __init__(self,name,age,salary):
        Employee.__init__(self,name,age)
        Salary.__init__(self,salary)
d=Database('Ambika',29,100000)
d.get_name()
d.get_age()
d.get_salary()


class Grandparent:
    def height(self):
        print("I have inherited my height from parent")
class Parent(Grandparent):
    def intelligence(self):
        print("I have inherited my height from parent")
class Child(Parent):
    def experience(self):
        print("I have 10 yrs exp")
Ch=Child()
Ch.intelligence()
Ch.experience()
Ch.height()


'''
Polymorphism
ability of an object to take many forms
'''
class Hominidare():
    def communication(self):
        print("hh")
    def walk(self):
        print("hk")
class Human(Hominidare):
    def communication(self):
        print("hk")
    def walk(self):
        print("hkf")
class Gorilla(Hominidare):
    def communication(self):
        print("hkoo")
    def walk(self):
        print("hkfjjj")
hm=Hominidare()
human1=Human()
gor=Gorilla()
hm.communication()
human1.communication()
gor.communication()
hm.walk()
human1.walk()
gor.walk()

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        print(self.__balance)
    def deposit(self,value):
        self.__balance=self.__balance+value
    def withdraw(self,value):
        self.__balance=self.__balance-value
class Currentaccount(BankAccount):
    def __init__(self,balance):
        super().__init__(balance)
    def withdraw(self,value):
        if(value>1000):
            print("contact bank manager")
        else:
            super().withdraw(value)

ca=Currentaccount(5000)
ca.get_balance()
ca.withdraw(4000)
ca.withdraw(999)
ca.get_balance()

class Employee:
    def __init__(self,name,age,basicsalary):
        self.__name=name
        self.__age=age
        self.__salary=basicsalary
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary
    def set_name(self,value):
        self.__name=value
    def set_age(self,value):
        self.__age=value
    def set_salary(self,value):
        self.__name=value
    def get_total_pay(self):
        pass
class FTemployees(Employee):
    def __init__(self,name,age,salary):
        super().__init__(name,age,salary)
    def get_total_pay(self):
        bonus=500
        return bonus+super().get_salary()
class Contractemployees(Employee):
    def __init__(self,name,age,salary):
        super().__init__(name,age,salary)
    def get_total_pay(self):
        bonus=250
        return bonus+super().get_salary()

dt=FTemployees('Sai',45,50000)
print(dt.get_name(),dt.get_age(),dt.get_salary(),dt.get_total_pay())
st=Contractemployees('Sai',45,50000)
print(st.get_name(),st.get_age(),st.get_salary(),st.get_total_pay())


