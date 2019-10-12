from exercisePack1.persondemo import Person

class Student(Person):
    def set_grade(self,grade):
        self.set_grade=grade
        return 1


if __name__=="__main__":
    toni = Student()
    toni.set_sex('wer')
    print(toni.sex)
    print(toni.get_sex)