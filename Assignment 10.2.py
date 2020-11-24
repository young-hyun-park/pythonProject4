file = input("Enter file name : ")
fn = open(file)
fn_list = list()
fn_dict = dict()
for i in fn:
    if i.startswith("From "):
        fn_split = i.split()
        fn_split2 = fn_split[5].split(":")
        fn_list.append(fn_split2[0])
for x in fn_list:
    if x not in fn_dict:
        fn_dict[x] = fn_dict.get(x,0)+1
    else:
        fn_dict[x] = fn_dict[x]+1
for k,v in sorted(fn_dict.items()):
    print(k,v)
