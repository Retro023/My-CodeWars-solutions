def odd_or_even(arr):
    sum_of_arr = sum(arr)
    if sum_of_arr % 2 == 0:
        return "even"
    else:
        return "odd"
    
#We first use the sum() method to get the sum of the array we then save that into a variable called sum_of_arr,
#Then we use a if statement to check if sum divided by 2 has a remiander of 0 if it does then the sum is even if,
#Not then the sum is odd we then return either even or odd





######TASK############
#Task:
#Given a list of integers, determine whether the sum of its elements is odd or even.

#Give your answer as a string matching "odd" or "even".

#If the input array is empty consider it as: [0] (array with a zero).

#Examples:
#Input: [0]
#Output: "even"

#Input: [0, 1, 4]
#Output: "odd"

#Input: [0, -1, -5]
#Output: "even"
#Have fun!
