class Person:
    name : str
    phonenumber : str
    emailaddress : str

    def __init__(self, ten,sdt, email) -> None:
        super().__init__()
        self.name = ten
        self.phonenumber = sdt
        self.emailaddress = email
    def outputPerson(self) -> str:
        inra = "Ten: " + self.name + "\t\nSDT: "+ self.phonenumber + "\t\nEmail: "+ self.emailaddress
        return inra

class Student(Person):
    studentnumber : str
    averagemark : float

    def __init__(self, ten, sdt, email, masinhvien, DTB) -> None:
        Person.__init__(self,ten, sdt, email)
        self.studentnumber = masinhvien
        self.averagemark = DTB
    def ouputStudent(self) -> str:
        inra = self.outputPerson() + "\tMa sinh vien: " + self.studentnumber + "\tDTB: " + self.averagemark
        return inra
class Professor(Person):
    Salary : float

    def __init__(self, ten,sdt,email,mucluong) -> None:
        Person.__init__(self,ten,sdt,email)
        self.Salary = mucluong
    def outputProfessor(self) -> str:
        inra = self.outputPerson() + "\tMuc luong: " + self.Salary
        return inra






