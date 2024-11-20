def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    
# We use a if elif statment to check the current colour of the traffic light we then return the correct colour based,
#on how a traffic light works so green > yellow > red > green etc
