hours = int(input("Enter total hours worked \n"))
rate = float(input("Enter pay rate \n"))

if hours <= 40:
    gross_pay = hours * rate
    print ("Gross pay: " + str(gross_pay))
else:
    overtime_rate = rate * 1.5
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * overtime_rate
    gross_pay = overtime_pay + (rate * 40)
    print("Gross pay: " + str(gross_pay))
