import random
target = random.randint(1,10)
print(target)
while True :
    userchoice = input("Enter the target number or Quit game by press Q  ")
    if(userchoice=="Q"):
        break
    userchoice = int(userchoice)
    if(userchoice==target):
        break
    elif(userchoice>target) :
        print("Number is small")
    else :
        print("Number is big")
print("____Game Over____")
    
    
