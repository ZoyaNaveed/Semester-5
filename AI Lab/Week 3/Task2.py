def balance_parenthesis(string):
	stack = []
	
	for c in string:
		if c == '(':
			stack.append(c)
		elif c == ')':
			if len(stack) > 0 and stack[-1] == '(':
				stack.pop()
			else:
				stack.append(c)
	return '(' * stack.count(')') + string + ')' * stack.count('(')

string = input("enter the input here: ")
print("Input:")
print(string)
adjusted_s = balance_parenthesis(string)
print("Balanced Parenthesis: ")
print(adjusted_s)

