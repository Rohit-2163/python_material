from operator import index, indexOf
def ifallnum(l):
    for i in l:
        if type(i)!=int:
            return False
    return True
def ifallstr(l):
    for i in l:
        if type(i)!=str:
            return False
    return True
def oddcount(l):
    count=0
    if(ifallnum(l)):
        for i in l:
            if i%2!=0:
                count+=1
        return count
    return "All Elements are not Integer"
def largestr(l):
    max=""
    if(ifallstr(l)):
        for i in l:
            if len(max)<len(i):
                max=i;
        return max
    return "All Elements are not String"
def rev(l):
    res=[]
    for i in range (0,len(l)):
        res.append(l[len(l)-i-1])
    return res

def find(l,element):
    for i in l:
        if i==element:
            return "element : <{}> present at index : {}".format(i,indexOf(l,i))
    return "element <{}> not present in the given list".format(element)
if __name__=='__main__':

    print("For Both Integer And String Type")
    print("--------------------------\n")
    l=[1,2,3,"hello","hehe",5,6,7,"namste indiaa"]
    print("ORIGINAL LIST                   :",l)
    # print("ALL ELEMENT IN LIST ARE NUMBER  :",ifallnum(l))
    print("NUMBER OF ODD ELEMENTS          :",oddcount(l))
    # print("ALL ELEMENT OF LIST ARE STRING  :",ifallstr(l))
    print("LARGEST STRING IN LIST          :",largestr(l))
    print("LIST IN REVERSE ORDER           :",rev(l))
    print(find(l,6))

    print("\n\nFor Only String Type")
    print("--------------------------\n")
    l=["hello","hehe","namste indiaa"]
    print("ORIGINAL LIST                   :",l)
    # print("ALL ELEMENT IN LIST ARE NUMBER  :",ifallnum(l))
    print("NUMBER OF ODD ELEMENTS          :",oddcount(l))
    # print("ALL ELEMENT OF LIST ARE STRING  :",ifallstr(l))
    print("LARGEST STRING IN LIST          :",largestr(l))
    print("LIST IN REVERSE ORDER           :",rev(l))
    print(find(l,"hehe"))
    
    print("\n\nFor Only Integer Type")
    print("--------------------------\n")
    l=[1,2,3,5,6,7]
    print("ORIGINAL LIST                   :",l)
    # print("ALL ELEMENT IN LIST ARE NUMBER  :",ifallnum(l))
    print("NUMBER OF ODD ELEMENTS          :",oddcount(l))
    # print("ALL ELEMENT OF LIST ARE STRING  :",ifallstr(l))
    print("LARGEST STRING IN LIST          :",largestr(l))
    print("LIST IN REVERSE ORDER           :",rev(l))
    print(find(l,6))
