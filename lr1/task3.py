def checkFormula(formula):
	"""
	This function checks if the user input matches the formula and returns the result
	"""
	#checks if the first element of a number
	if formula and formula[0].isdigit():
		formula = formula.lstrip('0123456789')
		if not formula:
			return True
		#checks if the element is a mathematical operation
		if formula[0] in '+-':
			return checkFormula(formula[1:])
	return False

if __name__ == "__main__":
	userFormula = input('Enter you formula: ')
	if checkFormula(userFormula):
		print('( True,', eval(userFormula), ')')
	else:
		print('( False, None )')

