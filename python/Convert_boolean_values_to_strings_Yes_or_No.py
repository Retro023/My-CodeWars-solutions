def bool_to_word(boolean):
    
    if boolean == True:
        boolean = "Yes"
    elif boolean == False:
        boolean = "No"
    else:
        print("No boolean value")
    return boolean

#we use an if statement to see if the variable boolean is either equal to True and False and then we change,
#Variable to either Yes for True and No for Flase then  we use an else staement incase the boolean variable is,
#Not a boolean value