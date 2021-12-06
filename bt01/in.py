from bttl import Person, Student,Professor
import pickle
#Nhap du lieu tu ban phim cho danh sach 10 Per,Stu,Pro
def main():
    nguoi = []
    hs = []
    gv = []
    count = 1
    while count <= 10:
        print("Person: ",count)
        nguoi.append(Person(input('Ten: '),input('SDT'), input('email: ')))
        print('Student: ', count)
        hs.append(Student(input('Ten: '),input('SDT'), input('email: '), input('masinhvien: '),input('DTB: ')))
        print('Professor: ', count)
        gv.append(Professor(input('Ten: '),input('SDT'), input('email: '), input('muc luong: ')))
        count = count +1

#In ket qua
    for i in range(9):
        print(nguoi[i].outputPerson())
        print(hs[i].ouputStudent())
        print(gv[i].outputProfessor())


#Sap xep theo de bai yeu cau
    for i in range(9):
        for j in range(i+1,9):
            if nguoi[i].name < nguoi[j].name:
                    nguoi[i],nguoi[j] = nguoi[j],nguoi[i]
            if hs[i].averagemark < hs[j].averagemark:
                    hs[i], hs[j] = hs[j], hs[i]
            if gv[i].Salary > gv[j].Salary:
                    gv[i], gv[j] = gv[j], gv[i]
#Pickle
    for i in nguoi:
        f1 = open('nguoi.txt', 'wb')
        pickle.dump(i.outputPerson(), f1)
        f1.close()


    for i in hs:
        f2 = open('hs.txt', 'wb')
        pickle.dump(i.ouputStudent(), f2)
        f2.close()

    for i in gv:
        f3 = open('gv.txt', 'wb')
        pickle.dump(i.outputProfessor(), f3)
        f3.close()

#Doc tap tin va in ra man hinh
    f1 = open('nguoi.txt', 'rb')
    a = pickle.load(f1)
    print(a)
    f1.close()

    f2 = open('hs.txt', 'rb')
    b = pickle.load(f2)
    print(b)
    f2.close()

    f3 = open('gv.txt', 'rb')
    c = pickle.load(f3)
    print(c)
    f3.close()

if __name__ == "__main__":
    main()

