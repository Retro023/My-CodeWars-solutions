def better_than_average(class_points, your_points):
    
    
    your_points = int(your_points)
    average = sum(class_points) / len(class_points)
    
    
    if your_points >= average:
        return True
    elif your_points <= average :
        return False
# calculates the sum of the class score then checks if your points are greater than or equal too if so,
#it returns True if your score  is less than or equal to the class average it returns False
# it also makes sure the variable your_points is a int