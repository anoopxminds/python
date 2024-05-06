#show_employee


def show_employee(Id, name, job_title, department, salary = 9000) :
    print("Employee ID : "+ str(Id));
    print("Employee Name : "+ str(name));
    print("Employee Job Title : "+ str(job_title));
    print("Employee Department : "+ str(department));
    print("Employee Salary : "+ str(salary));

show_employee(
    1001,
    "Anoop",
    "Developer",
    "IT",
    10000
);
