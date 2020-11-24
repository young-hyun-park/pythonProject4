hours=input("Enter hours:")
rate=input("Enter rate per hour:")
fh = float(hours)
fr = float(rate)
def computepay():
    if fh >= 40:
        pay = (40*fr)+(fh-40)*1.5*fr
    else:
        pay = fh*fr
    return pay

print("Pay",computepay())