# Q-1) Create a class Employee withn attributes empid, name, salary and also define methods to access properties of Employee ?

# -------Solution------>

class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary   
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
e1=Employee()
e2=Employee(1,"Rahul",40000)
e1.setEmpid(2)
e1.setName("Ramesh")
e1.setSalary(50000)
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())





# Q-2) Define a python class Person will instance object variables name and age. Set Instance object variables in __int__() method.
# Also define show() method to display name and age of a person.

# -----------Solution---------->

class Person:
    def __init__(self,name=None, age=None):
        self.name=name
        self.age=age
    def setName(self,name):
        self.name=name
    def setAge(self,age):
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
person1=Person("Amit",28)
person2=Person("Shubham",22)
print(person1.getName(),person1.getAge())
print(person2.getName(),person2.getAge())





# Q-3)Define a class Circle with instance object variable radius.
# Provide setter and getter for radius. Also define getArea() and getCircumference() methods.


# -----------Solution----------->

class Circle:
    def __init__(self,radius=None):
        self.radius=radius
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    def getArea(self):
        return(3.14*self.radius*self.radius)
    def getCircumference(self):
        return(2*3.14*self.radius)
c=Circle()
c.setRadius(4)        
print(c.getRadius(),c.getArea(),c.getCircumference())