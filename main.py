#1-masala
class School:
    def __init__(self, school_name, students):
        self.school_name = school_name
        self.__students = 0
        self.set_students(students)

    def get_students(self):
        return self.__students

    def set_students(self, new_students):
        if new_students > 10000:
            print("Juda ko'p o'quvchi")
        else:
            self.__students = new_students


s1 = School("45-maktab", 800)

print(s1.school_name)
print(s1.get_students())
