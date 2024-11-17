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
