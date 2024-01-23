student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermonie": 99,
    "Draco": 74,
    "Neville": 62
}

# TODO 1, CREATE AN EMPTY DICTONARY AND CALL IT STUDENT GRADES
student_grades = {}
# TODO 2, WRITE CODE TO ADD THE GRADES TO STUDENT GRADES
for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds"
    elif score > 70:
        student_grades[key] = "Acceptable"
    elif score < 70:
        student_grades[key] = "Fail"
"""
INSTRUCTIONS
SCORES ABOVE 90 = OUTSTANDING
SCORES ABOVE 80 = EXCEEDS
SCORES ABOVE 70 = ACCEPTABLE
SCORES BELOW 70 = FAIL
"""

print(student_grades)
