def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    
# We use a if elif statment to check the current colour of the traffic light we then return the correct colour based,
#on how a traffic light works so green > yellow > red > green etc




        
        
########TASK########        
        
#You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

#Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

#For example, when the input is green, output should be yellow.