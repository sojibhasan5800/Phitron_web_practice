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
    
        