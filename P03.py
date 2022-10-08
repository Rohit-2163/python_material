# fibonacci series: 0 1 1 2 3 5 8 13 _ _ _
def fiboAndFact(n):
    prevNum=0
    currentNum=1
    for i in range(1,n):
        prePrevNum=prevNum
        prevNum=currentNum
        currentNum=prevNum+prePrevNum
    return[currentNum , factorial(currentNum)]
   
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

if __name__ == '__main__':

    n = int(input("Enter value of n: "))
    [fib, fact]=fiboAndFact(n)
    
    print("Nth Fibonacci Term: {0}\nFactorial of Nth Term: {1}".format(fib, fact))
