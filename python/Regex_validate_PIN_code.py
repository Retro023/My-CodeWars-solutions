def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        return pin.isdigit()
    return False


# we check the length of the pin  using the len() method to make sure the pin is either 4 or 6 chars long,
#Then we use the isdigit() method to verify that the chars are all digits which if they all are digits it,
#returns True if the pin is nither it returns False




#####TASK#####

##ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#If the function is passed a valid PIN string, return true, else return false.

#Examples (Input --> Output)
#"1234"   -->  true
#"12345"  -->  false
#"a234"   -->  false
