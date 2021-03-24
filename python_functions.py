# greeting function

# # first iteration
# def greetings():
# 	print("Hello World!")

# greetings()

# # second iteration
# def greetings(name):
# 	print("Welcome on board " + name)

# greetings(input("What is your name? "))

# # third iteration
# def add(num1, num2):
# 	print(num1 + num2)

# add(23, 65434)

# # fourth iteration
# def diff(num1, num2):
# 	return num1 - num2
# 	code_here = None # nothing after the `return` gets executed

# print(diff(545, 321))

# create a calculator to add, subtract, divide and multiply
def calculator(operation, num1, num2):
	# taking user input
	operation = input("type the kind of operation that you want to perform (add, subtract, divide, multiply: ")
	num1 = input("type the first number: ")
	num2 = input("type the second number: ")

	# selecting the operation
	if operation == "add":
		print("the result of adding the two numbers you selected is:", str(num1 + num2))
	elif operation == "subtract":
		print("the result of subtracting the two numbers you selected is:", str(num1 - num2))
	elif operation == "divide":
		print("the result of dividing the two numbers you selected is:", str(num1 / num2))
	elif operation == "multiply":
		print("the result of multiplying the two numbers you selected is:", str(num1 * num2))
	else: # handle errors
		print("sorry, you didn't select a valid operation")

calculator()

# second iteration
def greetings(name):
	print("Salutations, " + name)

greetings(input("What is your name? "))