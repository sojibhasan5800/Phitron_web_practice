from abc import ABC,abstractmethod
class Subjects_Shape(ABC):
    @abstractmethod
    def __init__(self,subject_name,subject_teacher):
        self.subject_names = subject_name
        self.subject_teachers = subject_teacher
        self.max_marks=100
        self.pass_marks=33

    @abstractmethod
    def exam(self):
        pass
    

# Developer Function Below:
# System_Connection:

from teacher import Teachers
#--------------------------------

class Subject(Subjects_Shape):

    def __init__(self,subject_name,teacher_obj):
        self.subject_names = subject_name
        self.subject_teachers =  teacher_obj
        self.max_marks=100
        self.pass_marks=33

    
    def exam(self,students_lst_obj):
         for student in students_lst_obj:
            mark = self.teacher.evaluate_exam() # 50 -100
            student.marks[student.student_mark] = mark
            student.student_sub_grade[student.subject_name] = School.calculate_grade(mark)
        