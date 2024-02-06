#Error and Exception Handling

#try and except
print("1")
try:
    print("2")
except ValueError:
    print("4")
print("3")

#else
x = int(input("positive integer:"))
if x >= 0:
    pass
else:
    print("negative integer")
