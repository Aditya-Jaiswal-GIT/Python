with open("pratice.txt","w") as f:
    f.write("Java")
with open("pratice.txt","r") as f:
    data = f.read()
with open("pratice.txt","r") as f:
    new = data.replace("Java","Python")
with open("pratice.txt","w") as f:
    f.write(new)
with open("pratice.txt","r") as f:
    if(new.find("Python")!=-1):
        print("Found")
    else :
        print("Not found")
  