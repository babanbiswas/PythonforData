class employee():
    company_name = 'XYZ'

    def __init__(self, emp_name, emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    def changes(self, new_company_name):
        employee.company_name = new_company_name

    def info(self):
        print(f"Employee {self.emp_name} works for {self.emp_dept} in company {self.company_name}")

    @staticmethod
    def addition(x,y):
        print(x+y)

emp1 = employee('Baban','IT')
emp1.info()

emp2 = employee('Bob','HR')
emp2.info()
emp2.changes('Bob Marley Co')
emp2.info()

emp1.info()

emp1.addition(2,4)