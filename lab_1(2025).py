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

p1 = Me()
p1.name = "Vlad"
p1.seconary_name = "Tkachuk"
p1.year_of_birth = 2007
print(p1.return_course())
print(p1.name_second_name())
   