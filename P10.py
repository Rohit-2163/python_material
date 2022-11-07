def compute(string):
    obj = dict()
    print(obj)
    for i in string:
        print(obj)
        if i in obj:
            obj[i]+=1
        else:
            obj[i]=1
    print(obj)
    return obj
def displayFrequency(obj):
    for i in obj:
        print(f"Frequency of {i} is : {obj[i]}")
if __name__ == '__main__':
    string = str(input("Enter something : "))
    obj = compute(string)
    displayFrequency(obj)
    