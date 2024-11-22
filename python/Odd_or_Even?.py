def odd_or_even(arr):
    sum_of_arr = sum(arr)
    if sum_of_arr % 2 == 0:
        return "even"
    else:
        return "odd"
    
#We first use the sum() method to get the sum of the array we then save that into a variable called sum_of_arr,
#Then we use a if statement to check if sum divided by 2 has a remiander of 0 if it does then the sum is even if,
#Not then the sum is odd we then return either even or odd
