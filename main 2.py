score = input("Enter your score:")
try :
    fs = float(score)
except:
    print("Error. Enter numerical score")
    quit()
if fs >=0.9:
    print("A")
elif fs>=0.8:
    print("B")
elif fs>=0.7:
    print("C")
elif fs>=0.6:
    print("D")
else:
    print("F")
