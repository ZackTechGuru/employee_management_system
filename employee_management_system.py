class Employee:
    def __init__(self,employee_name, employee_id, employee_department, employee_salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_department = employee_department
        self.employee_salary = employee_salary
    def calculate_salary(self, employee_salary, hours_worked):
        overtime = 0
        if hours_worked >  50:
            overtime = hours_worked-50
        self.employee_salary = self.employee_salary + (overtime*(self.employee_salary/50))
    def assign_department(self, employee_department):
        self.employee_department = employee_department
    def print_employee_details(self):
        print("Name:", self.employee_name)
        print("ID:", self.employee_id)
        print("Department:", self.employee_department)
        print("Salary:", self.employee_salary)
        print("-----------------------------")
employee1 = Employee("Adam","23456","Finance", "KES 56,000")
employee2 = Employee("Jane","23457","Procurement", "KES 59,000")
employee3 = Employee("Lucy","23458","Accounts", "KES 60,000")
employee4 = Employee("John","23459","IT", "KES 67,000")
employee5 = Employee("Enock","23460","Operations", "KES 67,000")
employee6 = Employee("Steve","23461","Marketing", "KES 55,000")
employee7 = Employee("Elon","23462","Sales", "KES 50,000")
employee8 = Employee("Faith","23463","HR", "KES 70,000")

print("Employee details")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
employee5.print_employee_details()
employee6.print_employee_details()
employee7.print_employee_details()
employee8.print_employee_details()




