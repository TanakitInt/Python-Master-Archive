"""class"""
class Student(object):
    #define function in class
    def __init__(self, firstName, lastName):
        #your variable here
        self.firstName = firstName
        self.lastName = lastName
        self.id_number = 60070141

    def fullName(self):
        print(self.firstName, self.lastName)

    def validID(self, id_number):
        if 60070122 <= self.id_number <= 60070167:
            print("True")
        else:
            print("False")

def main():
    studentA = Student("Tanakit", "Intaniyom")
    studentA.fullName()
    studentA.validID(studentA.id_number)

if __name__ == '__main__':
    main()
