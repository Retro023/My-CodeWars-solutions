def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '/':
        try: 
            return value1 / value2
        except ZeroDivisionError:
                print("Error tried to dived by zero")
    elif operator == '*':
        return value1 * value2

# We use a elif block to check what operator is in use then we run the mathmatical operation against,
#Value1 and value2 based on what operators in use i,e if the operator is + we return value1 + value2,
#We also use a try and except for basic error catching in the divison part as we you cant divide by zero,
#This exception catches that error prints "Error tried to divide by zero" this saves the code from breaking




#####TASK########

#Your task is to create a function that does four basic mathematical operations.

#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.
#Examples(Operator, value1, value2) --> output

#('+', 4, 7) --> 11
#('-', 15, 18) --> -3
#('*', 5, 5) --> 25
#('/', 49, 7) --> 7

