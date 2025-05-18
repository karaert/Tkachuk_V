from datetime import datetime
class Me:
    def __init__(self, name=None, seconary_name=None, year_of_birth=None, ):
        self.course = None
        self.name = name
        self.seconary_name = seconary_name
        self.year_of_birth = year_of_birth
    def return_course(self):
        current_year = datetime.now().year
        self.course = current_year - (self.year_of_birth + 16)
       
        if self.course > 5:
            return "Сollege completed"
        else:
            return self.course
    def name_second_name(self):
        return [self.name, self.seconary_name]

class Student(Me):
    def __init__(self, name=None, seconary_name=None, year_of_birth=None,
                 group=None, faculty=None, university=None, gpa=None, email=None, phone=None):
        super().__init__(name, seconary_name, year_of_birth)
        self.group = group
        self.faculty = faculty
        self.university = university
        self.gpa = gpa
        self.email = email
        self.phone = phone

    def get_full_info(self):
        return {
            "name": self.name,
            "seconary_name": self.seconary_name,
            "year_of_birth": self.year_of_birth,
            "group": self.group,
            "faculty": self.faculty,
            "university": self.university,
            "gpa": self.gpa,
            "email": self.email,
            "phone": self.phone
        }

    def is_honors(self):
        if self.gpa >= 3:
            return True
        else:
            return False


student1 = Student(
    name="ivan",
    seconary_name="ivanov",
    year_of_birth=2007,
    group="IT-21",
    faculty="IT",
    university="KPI",
    gpa=4.7,
    email="email@email",
    phone="+380123456789"
)
print(student1.get_full_info())
print("Honors student:", student1.is_honors())