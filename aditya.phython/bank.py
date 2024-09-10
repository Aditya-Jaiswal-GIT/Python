class Bank :
    def __init__(self,balance,account) :
        self.balance = balance
        self.account = account
    def debit(self,amount) :
      self.balance =self.balance- amount
      print("Rs. ",amount,"Debited")
      c= self.get()
      print("Your balance is  : ",c)
    def credit(self,amount) :
        self.balance = self.balance+amount
        print("Rs. ",amount,"credited")
        d = self.get()
        print("Your balance is : ",d)
    def get(self) :
        return self.balance   
c1 = Bank(50000,12345)
c1.debit(200)
c1.credit(400)  

    

        