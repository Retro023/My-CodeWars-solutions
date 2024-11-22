def get_grade(s1, s2, s3):
    score = sum([s1, s2, s3]) / 3
    if 90 <= score <= 100:
        grade = "A"
    elif  80<= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif 0 <= score < 60:
        grade = "F"
    return grade

#we work out the average by first adding the variables s1, s2, s3 into a list then using the sum() method to,
#Workout the summary of the list then we divde the summary by 3 to work out the average we then store the output,
#Into a variable called score then using a if statement we check if the score is equal to the needed score of each grade,
# finally we create and update the value grade to the apropriate grade before finally returning the grade




####TASK####
#Grade book
#Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

#Numerical Score	Letter Grade
#90 <= score <= 100	'A'
#80 <= score < 90	'B'
#70 <= score < 80	'C'
#60 <= score < 70	'D'
#0 <= score < 60	'F'
#Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
