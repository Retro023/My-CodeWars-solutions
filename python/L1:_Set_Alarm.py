def set_alarm(employed, vacation):
    if employed and vacation == True:
        return False
    elif employed == True and vacation == False:
        return True
    elif employed == False and vacation == True:
        return False
    elif employed == False and vacation == False:
        return False
    
    
# We use a if elif statement to check the values of employed and vacation to see if they are either True of False
# based of the diagram we was given in the task we return either True of Flase based on boolean value of both employed 
# and vacation




####TASK#####


#Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. The first parameter, 
#employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

#The function should return true if you are employed and not on vacation, 
#(because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

#employed | vacation 
#true     | true     => false
#true     | false    => true
#false    | true     => false
#false    | false    => false
