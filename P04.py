def digits(n,s):
    if n==0:
        return s
    else:
        s.add(n%10)
        return digits(n//10,s)
    

Set=set()
userInput=int(input("enter number : "))
digits(userInput,Set)
print(Set)
    
    
