def is_isogram(string):
    cleaned_up = string.lower()
    check_istogram =  len(set(cleaned_up)) == len(cleaned_up)
    return check_istogram

#We first clean up the string to keep everything is kept consistent keeping the script running smoothly,
#Then we use the combined methods of len() and set() to calculate the number of unique characters in the string,
# we then compare that using ==  with the length of the string using the len() method again and if the length,
#of the unique string is the same length of the origanl string it must be a istogram we then save it as a varible,
# then return that variable.




#######TASK######
#An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#Implement a function that determines whether a string that contains only letters is an isogram. 
#Assume the empty string is an isogram. Ignore letter case.

#Example: (Input --> Output)
#"Dermatoglyphics" --> true
#"aba" --> false
#"moOse" --> false (ignore letter case)
