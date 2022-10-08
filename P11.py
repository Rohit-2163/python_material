# function of linear search parametres(list,finding value)
# if element not present in list return -1 index 
def linearSearch(lst,val):
    print("Result of linear serach :",end=" ")
    for i in range(len(lst)):
        if lst[i]==val:
            return i
    return -1
# function of binary search parameter(list , finding value)
# if element not present in list return -1 index 
def binarySearch(lst,val):
    lst.sort()
    print("Sorted list : ",lst)
    print("Result of binary serach :",end=" ")
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==val:
            return mid
        elif lst[mid]<val:
            low=mid+1
        else:
            high=mid-1
    return -1
# function of bubble sort 
def bubbleSort(lst):
    print("After bubble sort : ",end=" ")
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if(lst[j]>lst[j+1]):
                lst[j] ,lst[j+1]=lst[j+1],lst[j]
    return lst
# function of selection sort
def selectionSort(lst):
    print("After selection sort : ",end=" ")
    for i in range(len(lst)-1):
        min_ind=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_ind]:
                min_ind=j
        lst[min_ind],lst[i]=lst[i], lst[min_ind]
    return lst

# function of insertion  sort
def insertionSort(lst):
    print("After insertion sort : ",end=" ")
    for i in range(1,len(lst)):
        x=lst[i]
        j=i-1
        while j>=0 and x<lst[j]:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=x
    return lst

# function to print line
def line():
    print("------------------")
    print("------------------")

# funtion of  menu to make whole program menu driven makes easy to execute code by giving choice
def menu():
    print("1.linear search\n2.binary search\n3.bubble sort\n4.selection sort\n5.insertion sort\n6.exit")
    print()
    lst=[30,20,60,10,50,70,80,100,90,40]
    print("ORIGINAL LIST  : ",lst)
    line()
    choice=int(input("enter choice : "))
    if choice==1:
        val=int(input("Enter element to find : "))
        print("at index ",linearSearch(lst,val))
        line()
        menu()
    elif choice==2:
        val=int(input("Enter element to find : "))
        print("at index ",binarySearch(lst,val))
        line()
        menu()
    elif choice==3:
        print(bubbleSort(lst))
        line()
        menu()
    elif choice==4:
        print(selectionSort(lst))
        line()
        menu()
    elif choice==5:
        print(insertionSort(lst))
        line()
        menu()
    else:
        exit()

if __name__=='__main__':
    menu()
    
