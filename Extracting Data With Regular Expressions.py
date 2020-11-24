import re

fn =open("regex_sum_997801.txt")
x = 0
fn_list = list()
fn_read = fn.read()
fn_split = fn_read.split("\n")
for i in fn_split:
    first = re.findall('[0-9]+',i)
    fn_list = fn_list + first
for i in fn_list:
    x = x+ int(i)
print(x)
