#creating a class student
class Student:
    maxAvg=0
    def __init__(self,name,marks) :
        self.name = name
        self.marksList = marks
        self.setMaxAvg(marks)

    # function to calculate average marks of student and assing maxAvg to class variable 
    def setMaxAvg(self,marks) :
        avg = sum(marks)/len(marks)
        self.avg = avg
        Student.maxAvg = max(Student.maxAvg,avg)

    @staticmethod
    # function to return maxAvg and maxAvg is class variable
    def getMaxAvg():
        return Student.maxAvg
    
    # overriding __str__ function and printing student and their average marks as string
    def __str__(self) :
        res = "{0} : {1:.2f}".format(self.name,self.avg)
        return res
    
    # destructor to fee the memory when class object work is done
    def __del__(self):
        print("object deleted")

student1 = Student("student1",[89,40,80])
student2 = Student("student2",[77,99,60])
student3 = Student("student3",[81,20,50])

print(student1)
print()
print(student2)
print()
print(student3)
print()

print("The maximum average marks is : {0:.2f}".format(Student.getMaxAvg()))