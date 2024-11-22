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





####TASK#####
#There was a test in your class and you passed it. Congratulations!

#But you're an ambitious person. You want to know if you're better than the average student in your class.

#You receive an array with your peers' test scores. Now calculate the average and compare your score!

#Return true if you're better, else false!

#Note:
#Your points are not included in the array of your class's points. Do not forget them when calculating the average score!
