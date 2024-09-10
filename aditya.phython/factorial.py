def fact(n):
    i = n
    fact = 1
    while i>=1:
        fact = fact*i
        i=i-1
    print(fact)
    return fact
a = int(input("enter the number"))
fact(a)   
