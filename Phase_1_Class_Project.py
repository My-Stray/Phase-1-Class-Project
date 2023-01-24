#Justin Stevens CIS261 Phase 1

print("Welcome to Payroll\n")

def GetEmpName() -> str:
    empname = input("\nPlease enter employee's name, or press 0 to end : ")
    return empname
def hourlyrate() -> int:
    rate = input(float(input('Enter hourly rate : ',)))
    return hourlyrate
def taxrate() -> int:
    input('Enter tax rate : ', .2)
    return taxrate
def Totalhours() -> int: 
    float(input("Enter hours worked : "))
    return Totalhours
def reghours():
    reghours = (float(Totalhours) - (overtimehours),)
def regpay():
    float(reghours * hourlyrate, .2)
def overtimehours():
    overtimehours = (float(Totalhours - 40))
def overtimerate():
    float(hourlyrate * 1.5, .2)
def overtimepay():
    float(overtimehours * overtimerate)
    return overtimepay
def incometax() -> int:
    return (float(grosspay * taxrate, .2))
def grosspay():
    float(regpay + overtimepay, .2)
    return grosspay
def netpay():
   float(grosspay - incometax, .2)
   while True:
        if Totalhours < 40:
            print("empname: ")
            print("Totalhours: ",.2)
            print("reghours: ",.2)
            print("hourlyrate: ",.2)
            print("regpay: ",.2)
            print("Overtime hours: 0")
            print("Overtimerate: ")
            print("Overtime Pay: $0.00")
            print("Gross Pay: $", .2)
            print('incometax $', 2)
            print('netpay: $', 2)
        else: 
            print("Employee's name: ", )
            print("Totalhours: ")
            print("reghours(): ")
            print("hourlyrate(): ")
            print("regpay: ")
            print("Overtime hours: ")
            print("Overtimerate: $ ", .2)
            print("Overtime Pay: $ , .2")
            print("Gross Pay: $ ", )
            print('incometax: $ ', .2)
            print("netpay: $ ", .2\n)
        def anotherentry() -> str:
            return "Do you want to add another employee? Enter yes or no :"
            if anotherentry == yes:
               return GetEmpName()
            else:
                def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
                    print(f"Total Number Of Employees: {TotEmployees}")
                    print(f"Total Hours Worked: {Totalhours:,.2f}")
                    if __name__ == "__main__":
                        TotEmployees = 0
                        TotHours = 0.00
                        TotGrossPay = 0.00
                        TotTax = 0.00
                        TotNetPay = 0.00
                    while True:
                        GetEmpName()
                        if (empname.upper() == "END"):
                            break

    
