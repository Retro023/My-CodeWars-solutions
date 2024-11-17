def find_average(numbers):
    if len(numbers)  == 0:
        return 0
    average = sum(numbers) / len(numbers)
    return average

# we first use the len() method to check if the length of the numbers is equal to 0 if it is then we return 0,
# then we work out the average by using the sum() to workout the summary numbers then we divide it bu the length,
#Of the numbers saving the output to the variable average which then we return