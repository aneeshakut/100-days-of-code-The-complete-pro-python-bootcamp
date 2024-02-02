#Filtering Even numbers

list_of_strings = input("Enter a few numbers:").split(',')
numbers = [int(x) for x in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)
