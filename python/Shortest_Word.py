def find_short(s):
    return len(min(s.split(" "), key=len))
  
    
#First we split the words by space (allowing us to use the separately),
# We then use the min() method with its key paramater to sort the words by there length,
#Finally we use the len() method to get the shortest words length in intergers





#####TASK######
#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.
