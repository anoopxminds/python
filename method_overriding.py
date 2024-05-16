#Create a class Employee with name and qualification,experience,salary.
#Create sub classes Doctor with noOfPatients property.and NursingStaff 
#Employee contains a method totalSalary which will return the salary of employees.
#Override the method in Doctor and NursingStaff.
#Doctor will get an additional salary of 150Rs for each extra patients in a day
#NursingAssistant will get 100Rs per hour for extra hours he works


class Employee:
    def __init__(self, name, qualification, experience, salary):
        self.name = name
        self.qualification = qualification
        self.experience = experience
        self.salary = salary
        
    def totalSalary(self):
        #print(f"Salary : {self.salary}")
        return self.salary;

class Doctor(Employee):
    noOfPatients = 4
    def __init__(self, name, qualification, experience, salary):
        super().__init__(name, qualification, experience, salary)
       
    def totalSalary(self):
         #calculating doctor salary
        net_salary = super().totalSalary() + (150 * self.noOfPatients)
        return net_salary
    
    def display_details(self):
        print(f"Doctor Name : {self.name}")
        print(f"Doctor Qualification : {self.qualification}")
        print(f"Doctor Experience : {self.experience}")
        print(f"Doctor Salary : {self.totalSalary()}")
    
class NursingStaff(Employee):
    extra_hours = 3
    def __init__(self, name, qualification, experience, salary):
        super().__init__(name, qualification, experience, salary)
        
    def totalSalary(self):
        total_salary = super().totalSalary() + (100 * self.extra_hours)
        return total_salary
    
    def display_details(self):
        print(f"Nursing Staff Name : {self.name}")
        print(f"Nursing Staff Qualification : {self.qualification}")
        print(f"Nursing Staff Experience : {self.experience}")
        print(f"Nursing Staff Salary : {self.totalSalary()}")
        
        
employee1 = Employee("Doctor Name", "MBBS", 2, 100000);
employee2 = Employee("Nursing staff Name", "BSC", 4, 40000);
doctor = Doctor(employee1.name, employee1.qualification, employee1.experience, employee1.salary)
doctor.display_details()
nursing_staff = NursingStaff(employee2.name, employee2.qualification, employee2.experience, employee2.salary)
nursing_staff.display_details()   
    