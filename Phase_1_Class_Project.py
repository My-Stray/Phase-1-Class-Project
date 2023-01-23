#Justin Stevens CIS261 Phase 1

print("Welcome to Payroll\n")

def GetEmpName() -> str:
    empname = input("\nPlease enter employee's information, or press 0 to end : ")
def reghours():
    reghours = (float(hoursworked) - (overtimehours),)
def overtimehours():
    overtimehours = (float(hoursworked - 40))
def GetHoursWorked():
    hoursworked = (float(input("Enter hours worked : ")))
def totalhours():
    totalhours = hoursworked
    return totalhours
def hourlyrate() -> int:
    return (float(input('Enter hourly rate: ',)))
def taxrate() -> int:
    return (float(intput('Enter tax rate: ',)))
def incometax() -> int:
    incometax = (float(input(grosspay * taxrate, 2)))
def CalcTaxAndNetPay(hours: int, hourlyrate: int, taxrate: int):
    while True:
        if hours < 40:
            print("Employee's name: ", empname)
            print("totalhours: ")
            print("reghours: ")
            print("hourlyrate: ")
            regpay = (reghours * hourlyrate, 2)
            print("regpay: ")
            print("Overtime hours: 0")
            overtimerate = (hourlyrate * 1.5, 2)
            print("Overtimerate: ")
            print("Overtime Pay: $0.00")
            grosspay = regpay
            print("Gross Pay: $", regpay)
            def incometax():
                incometax= (float(grosspay * taxrate, 2))
            netpay = (grosspay - incometax, 2)
            print('incometax $', 2)
            print ('netpay $', 2)
        else: 
            print("Employee's name: ", empname)
            print("totalhours: ")
            print("reghours: ")
            print("hourlyrate: ")
            regpay = (reghours * hourlyrate, 2)
            print("regpay: ")
            print("Overtime hours: ")
            overtimerate = (hourlyrate * 1.5, 2)
            print("Overtimerate: ")
            print("Overtime Pay: $ , 2")
            grosspay = regpay
            print("Gross Pay: $ ", regpay)
            def incometax():
                incometax= (float(grosspay * taxrate, 2))
            netpay = (grosspay - incometax, 2)
            print('incometax $ ', 2)
            print ('netpay $ ', 2)
        def anotherentry():
            anotherentry = input("Do you want to add another employee? Enter yes or no :")
            if yes:
                GetEmpName
            else:
                print("Closing Paroll, Goodbye")
                end


