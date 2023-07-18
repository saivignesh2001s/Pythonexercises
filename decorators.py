def asterisk(func):
    def highlight():
        print('*'*50)
        func()
        print('*'*50)
    return highlight


def plus(func):
    def highlight():
        print('+'*50)
        func()
        print('+'*50)
    return highlight

@plus
@asterisk
def mass():
    print('sai')
def check_length(func):
    def calculate(name):
        if len(name)>6:
             raise ValueError
        return func(name)
    return calculate
@check_length
def college_student(collegename):
    students=[]
    @check_length
    def add_student(studentname):
        students.append(studentname)
        print("students in", collegename, "is", students)
    return add_student

studentyale=college_student('yale')
studentyale('sai')
studentduke=college_student('duke')
studentduke('saivignesh')
studentduke=college_student('Berkley')

'''
Decorators add functionality without modifying the code
We use closures
Closures are nested functions which revolves around local variables
'''
