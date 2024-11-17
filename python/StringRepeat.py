def repeat_str(repeat, string):
    repeated_str = int(repeat) * string
    return repeated_str

#we use the int() method to make sure the repeat variable is a int then we times it by the string and as the string,
#Is not a int but a str it will repeat its self x amount of times so if reapeat = 3 and string = hello,
# the out put would be hellohellohello then we save that into a variable called repeated_str and finally return that variable