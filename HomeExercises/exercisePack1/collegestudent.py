from exercisePack1.student import Student

class CollegeStu(Student):

    def __init__(self,name,sex,province):
        Student.__init__(self,name,sex,province)

    def has_peer(self):
        return self.peer

    def set_peer(self,peer=None):
        if peer:
            self.peer=True
        else:
            self.peer=False

if __name__=='__main__':
    toni = Student()
    toni.set_sex('wer')
    print(toni.sex)
    print(toni.get_sex)