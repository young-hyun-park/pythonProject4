hours = input("Enter hours:")
rate_per_hour = input("Enter rate per hour:")
try:
    fh = float(hours)
    fr = float(rate_per_hour)
except:
    print("Error, please enter numeric input")
    quit()

if fh > 40:
    pay = 40 * fr + (fh - 40) * fr * 1.5
else:
    pay = fh * fr
print(pay)
