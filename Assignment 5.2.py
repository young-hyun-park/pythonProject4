largest = None
smallest = None
while True:
    num = input("Enter the number:")
    try:
        fn = int(num)
    except:
        if num == "Done":
            break
        print("Invalid input")
        continue
    if largest is None:
        largest = fn
        smallest = fn
    elif largest <= fn:
        largest = fn
    elif smallest >= fn:
        smallest = fn
print("Maximum is",largest)
print("Minimum is",smallest)