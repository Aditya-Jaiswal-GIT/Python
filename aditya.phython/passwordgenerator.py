import random
import string
val = string.ascii_letters + string.digits + string.punctuation
length = 12
password = ""
for i in range(length):
    password = password + random.choice(val)
print("Your password is : ",password)
