
while True:
    fname = input("Enter file name:")
    try:
        fh = open(fname)
    except:
        print("Enter the right file name")
        continue
    for line in fh:
        a = fh.read()
        b= a.rstrip()
        c=b.upper()
        print(c)
    quit()