file = input("Enter file name:")
fn = open(file)
fn_list = list()
count = 0
for line in fn:
    if line.startswith("From "):
        fn_split = line.split()
        fn_list.append(fn_split[1])
        count = count + 1
for line in fn_list:
    print(line)
print("There were",count,"lines in the file with From as the first word")