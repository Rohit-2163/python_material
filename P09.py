def userInput(obj):
    marks = list()
    name  = str(input("Enter the name of student : "))
    for i in range(4):
        value = int(input(f"Enter marks of subject {i+1} : "))
        marks.append(value)
    obj[name] = marks
    print()

def scoredMax(obj):
    maxValue = 0
    for key in obj:
        total = sum(obj[key])
        if total > maxValue:
            maxValue = total
            student = key
    return student

if __name__ == '__main__':
    obj = dict()
    n = int(input("Enter no of students: "))
    for i in range(n):
        userInput(obj)
    print(obj)
    print(scoredMax(obj))
    


    