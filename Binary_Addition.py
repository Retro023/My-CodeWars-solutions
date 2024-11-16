def add_binary(a,b):
    summary = sum([a, b])
    binary = bin(summary).replace("0b", "")
    return binary

# we first use the sum() method to work out the sum of variables a and b then save it to a variable called summary,
# Then we use the bin() method to convert the summary to binary and we use the replace() method to replace,
#The 0b prefix with a empty string only leaving the binary digits we finally save the output to a variable and,
#Return it
