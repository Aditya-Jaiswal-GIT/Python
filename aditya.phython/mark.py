class Student :
    def __init__(self,maths,science,english,name) :
        self.name = name
        self.english = english
        self.maths = maths
        self.science = science
    def average(self) :
        average = (self.maths+self.science+self.english)/3
        print("Welcome ",self.name)
        print("The average is  : ",average)

s1 = Student(34,50,44,"Aditya")
s1.average()
    