def add_binary(a,b):
    summary = sum([a, b])
    binary = bin(summary).replace("0b", "")
    return binary

# we first use the sum() method to work out the sum of variables a and b then save it to a variable called summary,
# Then we use the bin() method to convert the summary to binary and we use the replace() method to replace,
#The 0b prefix with a empty string only leaving the binary digits we finally save the output to a variable and,
#Return it




#####TASK#####

#Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
#The binary number returned should be a string.

#Examples:(Input1, Input2 --> Output (explanation)))
#1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
#5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
