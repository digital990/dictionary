student_scores = {
    "David": 90,
    "Mike": 78,
    "Precious": 99,
    "Bola": 74,
    "charles": 62
}

student_grades = {}
# write your code to grade your students

for x in student_scores:
    score = student_scores[x]
    if score > 90:
        student_grades[x] = "Outstanding"
    elif score > 80:
        student_grades[x] = "Exceeds"
    elif score > 70:
        student_grades[x] = "Acceptable"
    elif score < 70:
        student_grades[x] = "Fail"

print(student_grades)