import unittest as uni

def split_input(grade):
    temp = [ ]
    grade = grade.split(",")

    for i in grade:
        if i.isdigit() == True:
            i = float(i)
            temp.append(i)
        elif isinstance(i, str) == True:
            i = i.lower()
            temp.append(i)
    grade = temp

    return grade

def verify_grade(grade):
    error = [ ]
    valid = [ ]

    for i in grade:
        #'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F' not included ; converted at split_input.
        if i not in ['a', 'b+', 'b', 'c+', 'c', 'd+', 'd', 'f',\
         4, 4.0, 3.5, 3, 3.0, 2.5, 2, 2.0, 1.5, 1, 1.0, 0, 0.0]:
            error.append(i)
        else:
            valid.append(i)
    grade = valid

    return grade 

def map_grade(grade):
    temp = [ ]

    for i in grade:

        #'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F' not included ; converted at split_input.
        #for upper case
       #if i == 'A':
       #    i = 4.0
       #    temp.append(i)
       #elif i == 'B+':
       #    i = 3.5
       #    temp.append(i)
       #elif i == 'B':
       #    i = 3.0
       #    temp.append(i)
       #elif i == 'C+':
       #    i = 2.5
       #    temp.append(i)
       #elif i == 'C':
       #    i = 2.0
       #    temp.append(i)
       #elif i == 'D+':
       #    i = 1.5
       #    temp.append(i)
       #elif i == 'D':
       #    i = 1.0
       #    temp.append(i)
       #elif i == 'F':
       #    i = 0.0
       #    temp.append(i)

        #for lower case ; included from converted Big alphabet.
        if i == 'a':
            i = 4.0
            temp.append(i)
        elif i == 'b+':
            i = 3.5
            temp.append(i)
        elif i == 'b':
            i = 3.0
            temp.append(i)
        elif i == 'c+':
            i = 2.5
            temp.append(i)
        elif i == 'c':
            i = 2.0
            temp.append(i)
        elif i == 'd+':
            i = 1.5
            temp.append(i)
        elif i == 'd':
            i = 1.0
            temp.append(i)
        elif i == 'f':
            i = 0.0
            temp.append(i)

        #4, 3, 2, 1, 0 not included ; converted at split_input.
        #for interger            
       #elif i == 4:
       #    i = 4.0
       #    temp.append(i)
       #elif i == 3:
       #    i = 3.0
       #    temp.append(i)
       #elif i == 2:
       #    i = 2.0
       #    temp.append(i)
       #elif i == 1:
       #    i = 1.0
       #    temp.append(i)

        #for float (by its native)
        else:
            temp.append(i)

    grade = temp         

    return grade

def cal_gpa(grade):

    gradeSumation = sum(grade)
    gradeLength = len(grade)

    gpa = gradeSumation/gradeLength

    grade = gpa
    
    return grade

def main(grade):
    grade = split_input(grade)
    grade = verify_grade(grade)
    grade = map_grade(grade)
    grade = cal_gpa(grade)

class CaseTest(uni.TestCase):
        #self.assertEqual(function(...input...,...Output...))
    def test1(self):
        self.assertEqual(split_input("A,B+,b,4"),['a', 'b+', 'b', 4.0])
    def test2(self):
        self.assertEqual(verify_grade(['a', 'b+', 'b', 4.0, 'itsAnErrorHere!']),['a', 'b+', 'b', 4.0])
    def test3(self):
        self.assertEqual(map_grade(['a', 'b+', 'b', 4.0]),[4.0, 3.5, 3.0, 4.0])
    def test4(self):
        self.assertEqual(cal_gpa([4.0, 3.5, 3.0, 4.0]),3.625)

if __name__ == '__main__':
    uni.main()
