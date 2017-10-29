def grade_calculator(total, obtained):
    percentage = ((obtained * 100) / total)
    grade = ""
    if percentage >= 70:
        grade = "A"
    if percentage >= 60 and percentage < 70:
        grade = "B"
    if percentage >= 50 and percentage < 60:
        grade = "C"
    if percentage >= 40 and percentage < 50:
        grade = "D"
    if percentage < 40:
        grade = "Fail"
    return grade
