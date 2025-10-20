class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._department="IT"
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,amount):
        if amount<0:
            self.__salary=amount
        else:
            print("Invalid amount")

emp1=Employee("Anoop",30000)
print(emp1.name)

# Access private attribute directly
# print(emp1.__salary)    Attribute error

#Can access protected member but not recommendeds
print(emp1._department)

print(emp1.get_salary())

new_salary=35000

emp1.set_salary(new_salary)

print(emp1.get_salary())

    
    

        