class Me:
    def __init__(self, name, seconary_name, year_of_birth):
        self.name = name
        self.seconary_name = seconary_name
        self.year_of_birth = year_of_birth
    def name_second_name(self):
        return [self.name, self.seconary_name]

p1 = Me("Vlad", "Tkachuk", 2007)

print(p1.name_second_name())

        

   