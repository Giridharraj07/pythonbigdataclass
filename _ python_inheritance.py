# inheritance in python
# Base Class aka parent class
# class person():

#     def __init__(self,name):
#         self.name = name

#     def displayName(self):
#         print(self.name) 


#     # By default we can say that particular person is unemployed
#     def isEmployed(self):
#         print(self.name,"is Un-Employed!!")

# # Derived Class aka child class
# class Employee(person):
    
#     def isEmployed(self):
#         print(self.name,"is Employed!!") 


# emp =person('Raj')   
# emp.displayName()       
# emp.isEmployed()

# emp1=person('Giridhar')   
# emp1.displayName()       
# emp1.isEmployed()

# how to initialize constructor of base class
class person():

    def __init__(self,name):
        self.name = name

    def displayName(self):
        print(self.name) 


    # By default we can say that particular person is unemployed
    def isEmployed(self):
        print(self.name,"is Un-Employed!!")

# Derived Class aka child class
class Employee(person):
    def __init__(self, emp_name,id_num,salary,designation):
        self.idnumber =id_num
        self.emp_salary=salary
        self.emp_designation =designation
        person.__init__(self, emp_name)
       
        #calling constructor of base class
        #person.__init__(self, emp_name)
        super().__init__(emp_name)
      

    def isEmployed(self):
        print(self.name,"is Employed!!") 
    
    def employeedetails(self):
        print("Employee id is",self.idnumber,
        "Employee Salary is",self.emp_salary,
        "Employee Designation is",self.emp_designation)

# emp =person('Raj')   
# emp.displayName()       
# emp.isEmployed()
# emp.emp_salary
# emp.employeedetails()

emp1 = Employee('Raj', 5431, 1000, 'Data Engineer')
emp1.displayName()       
print(emp1.name)
emp1.employeedetails()

  


