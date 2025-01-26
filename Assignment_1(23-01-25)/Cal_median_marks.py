"""Q3. You are a teacher and you have the scores of your students on a test. The scores are stored in a list. Your task is to write a Python program to find the median score. 
If the number of scores is even, the median is the average of the two middle scores."""

Student_score = [56, 72, 89, 65, 47, 90, 78, 84]
Student_score.sort()
n = len(Student_score)
if n % 2 == 1:
    # If the number of scores is odd the median is the middle element
    median = Student_score[n // 2]
else:
    # If the number of scores is even the median is the average of the two middle elements
    median = (Student_score[n // 2 - 1] + Student_score[n // 2]) //2
print(f"The sorted scores are: {Student_score}")
print(f"The median score is: {median}")
