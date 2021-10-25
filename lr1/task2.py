from sys import argv

if __name__ == "__main__":
	#dictionary of mathematical operations
	dictOperatorType = {'add': '+', 'addition': '+', 'sub': '-', 'subtraction': '-', 
	'mul': '*', 'multiplication': '*', 'div': '/', 'division': '/'}
	#Checking the correctness of the input
	if len(argv) == 4 and argv[1] in dictOperatorType and argv[2].isdigit() and argv[3].isdigit():
		try:
			print(eval(argv[2] + dictOperatorType[argv[1]] + argv[3]))
		except ZeroDivisionError:
			#Division by zero error
			print('Division by zero')
	else:
		print('Incorrect input')