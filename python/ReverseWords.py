def reverse_words(text):
    reversed =  ' '.join(word[::-1] for word in text.split(' '))
    return reversed

# we  first split each word by space then we reverse each word and then we join it back with spaces beifre finally,
#saving the output to a variable called reversed and then returning that value






#####TASK#####
#Complete the function that accepts a string parameter, 
#and reverses each word in the string. All spaces in the string should be retained.

#Examples
#"This is an example!" ==> "sihT si na !elpmaxe"
#"double  spaces"      ==> "elbuod  secaps"
