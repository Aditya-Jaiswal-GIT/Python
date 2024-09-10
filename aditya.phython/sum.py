def sum(n):
   s = 0
   if(n==0) :
      return 0 

   return sum(n-1) + n
a = sum(5)
print(a)


   
    
    
