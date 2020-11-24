fname = input("Enter file name:")
fn = open(fname)
fn_list = list()
fn_read = fn.readlines()
for line in fn_read:
    fn_split = line.split()
    for i in fn_split:
        if i not in fn_list:
            fn_list.append(i)
fn_list.sort()
print(fn_list)