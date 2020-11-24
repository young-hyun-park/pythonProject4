hours = input("Enter hours:")
rate_per_hour = input("Enter rate per hour:")
if float(hours)>40:
    pay = 40*float(rate_per_hour)+(float(hours)-40)*float(rate_per_hour)*1.5
else:
    pay = float(rate_per_hour)*float(hours)
print(pay)