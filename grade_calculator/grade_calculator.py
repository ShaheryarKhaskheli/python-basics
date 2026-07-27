def cal_avg(total, subjects=5):
    return total / subjects

def det_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

subject = 5
total = 0
for i in range(1, subject + 1):
    marks = float(input(f"Subject {i}: "))
    total += marks

average = cal_avg(total, subject)
grade = det_grade(average)

print("Summary For Grade")
print("total marks", total)
print("average ", average)
print("grade = ", grade)