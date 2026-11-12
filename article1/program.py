import hr

salary_employee = hr.SalaryEmployee(1, "John Smith", 1500)
hourly_employee = hr.HourlyEmployee(2, "Yassine Delivery", 6, 18.50)
hourly_employee_2 = hr.HourlyEmployee(3, "Yassine Tutoring", 2.5, 32.00)
commission_employee = hr.CommissionEmployee(4, "Kevin Bacon", 1000, 250)

payrol_system = hr.PayrollSystem()
payrol_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    hourly_employee_2,
    commission_employee
])