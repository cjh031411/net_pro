class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age,employeeId):
        super().__init__(name, age)
        self.employeeId=employeeId

    def getID(self):
        print(self.employeeId)

iot=Employee("IoT",65,2018)

iot.getName()
iot.getAge()
iot.getID()