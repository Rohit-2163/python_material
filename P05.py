from P03 import factorial
def calcSeries(x,n):
    sum=0
    sing=1
    for i in range (0,n+1):
        if(i%2==0):
            sum=sum+(sing*((x**i)/(factorial(i))))
            sing=-sing
    return sum

if __name__=='__main__':
    n = int(input("Enter the value of n : "))
    x = int(input("Enter value of x: "))
    print(calcSeries(x,n))

