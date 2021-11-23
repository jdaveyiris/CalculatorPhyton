"""
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
operator = input("Enter operator:")

if operator == "+":
    result = first_number + second_number
if operator == "-":
    result = first_number - second_number
if operator == "*":
    result = first_number * second_number
if operator == "/":
    result = first_number / second_number

print(f"Equals: {result}")

#------

total = 0
with open("step_2.txt", 'r') as f:
    lined_text = f.read().splitlines()
    
for x in lined_text:
    split_line = x.split()

    first_number = int(split_line[2])
    second_number = int(split_line[3])
    operator = split_line[1]
    
    
    if operator == "+":
        result = first_number + second_number
        total = total + result
        print(f"Equals: {result}")
    if operator == "-":
        result = first_number - second_number
        total = total + result
        print(f"Equals: {result}")
    if operator == "x":
        result = first_number * second_number
        total = total + result
        print(f"Equals: {result}")
    if operator == "/":
        result = first_number / second_number
        total = total + result
        print(f"Equals: {result}")

print(f"Total: {total}")

"""

with open("step_3.txt", 'r') as f:
    lined_text = f.read().splitlines()
    first_line = f.readline()

split_line = first_line.split()
where_to_go = split_line[1]
current_line = first_line


if where_to_go == "calc":
    first_number = int(split_line[4])
    second_number = int(split_line[5])
    operator = split_line[3]

    if operator == "+":
        result = first_number + second_number
        current_line = f.readline(result)
    if operator == "-":
        result = first_number - second_number
        current_line = f.readline(result)
    if operator == "x":
        result = first_number * second_number
        current_line = f.readline(result)
    if operator == "/":
        result = first_number / second_number
        current_line = f.readline(result)

if where_to_go != "calc":
    result = (split_line[1])
    current_line = f.readline(result)

if current_line == where_to_go:
    print(f"Endline is: {where_to_go}")