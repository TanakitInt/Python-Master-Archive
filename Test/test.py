"""This is docstring"""
def main():
    """Grading system"""
    point = 0
    l1st = []
    while point >= 0:
        point = int(input())
        if point > 100:
            grade = "Error"
        elif point >= 80 and point <= 100:
            grade = "A"
        elif point >= 75 and point < 80:
            grade = "B+"
        elif point >= 70 and point < 75:
            grade = "B"
        elif point >= 65 and point < 70:
            grade = "C+"
        elif point >= 60 and point < 65:
            grade = "C"
        elif point >= 55 and point < 60:
            grade = "D+"
        elif point >= 50 and point < 55:
            grade = "D"
        elif point >= 0 and point < 50:
            grade = "F"
        else:
            break
        l1st.append(grade)
    for i in l1st:
        print(i)
main()
