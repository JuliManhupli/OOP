from sys import argv

operators = ['+', '-', '*', '/']

if __name__ == "__main__":
	#Checking the correctness of the input
	if len(argv) == 4 and argv[1].isdigit() and argv[2] in operators and argv[3].isdigit():
		try:
			print(eval(argv[1] + argv[2] + argv[3]))
		except ZeroDivisionError:
			#Division by zero error
			print('Division by zero')
	else:
		print('Incorrect input')