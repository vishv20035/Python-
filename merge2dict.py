mydict1={}
print("Enter the elements of first dic")
while True:
        key=input("Enter a key(or 'q' to quit):")
        if key=='q':
            break
        value=int(input("Enter a value:"))
        mydict1[key]=value
print("Enter the elements of second dic")
mydict2={}
while True:
        key=input("Enter a key(or 'q' to quit):")
        if key=='q':
            break
        value=int(input("Enter a value:"))
        mydict2[key]=value
print(mydict1| mydict2)
