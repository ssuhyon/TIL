class Student:
    '''
    후.....
    하기 싫다..
    '''
    scholarship_score = 80


    def __init__(self, name, age, grade, score):
        self.name = name
        self.age = age
        self.grade = grade
        self.score = score

    def get_grade(self):
        print(f'called >>>> get_grade')
        return f'return >>>> {self.grade}'
    
    def jojung():
        Student.scholarship_score = 85

a = ('sh',32,2)
print(Student.scholarship_score)