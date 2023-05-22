class Employee:
    
    #class attribute
    empCount = 0

    # constructor of class
    # constructor  mainly used for assignment of instance variables
    def __init__(self, name, salary):
        #instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary
        Employee.empCount += 1

    # method of a class
    def displayEmployeeInfo(self): 
       print("Employee name :",self.emp_name," ,Employee salary :",self.emp_salary)

    # method of class
    def displayEmployeeCount(self): 
       print("Employee Count :",Employee.empCount)

emp1 = Employee('giridhar',1000)
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

emp2 = Employee('tarun', 2000)
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()

emp1.displayEmployeeCount()
emp2.displayEmployeeCount()

