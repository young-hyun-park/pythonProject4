fname = input("Enter file name:")
fn = open(fname)
b=0.0
count= 0.0
for line in fn :
    if  line.startswith("X-DSPAM-Confidence"):
        a = float(line[20:])
        b = a + b
        count= count+1.0
print(b/count)