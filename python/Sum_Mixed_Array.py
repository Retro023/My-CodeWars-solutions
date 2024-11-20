def sum_mix(arr):
    int_arr = [int(i) for i in arr]
    return sum(int_arr)

#we use a list comprehension to itterate each element i in the array for each elemment it converts it to a integer,
#Using the int() method the result is a new list saved as a variable called int_arr we use the sum() method to calcualte the sum,
# Of the list we then return that sum
