def sum_array(arr):
    
    if not arr or len(arr) < 3:
        return 0
    else:
        sorted_arr = sorted(arr)
        summary = sum(sorted_arr[1:-1])
        return summary
    
    #First we handle None arrays with fewer elements then 3 if they are we return 0,
    #Then we sort the array highest to lowest and then save it to a variable called sorted_arr after which we use the,
    #sum() method to work out the summary and remove the smallest and largest element finally we save it to a,
    #Variable summary and return that variable



####TASK######

#Task
#Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

#The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

#Mind the input validation.

#Example
#{ 6, 2, 1, 8, 10 } => 16
#{ 1, 1, 11, 2, 3 } => 6
#Input validation
#If an empty value ( null, None, Nothing, nil etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
