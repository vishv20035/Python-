list1=[]
list2 =[]
n1 = int(input("Enter the limit list 1"))

for i in range(0,n1):
    value=int(input("Enter the value\n"))
    list1.append(value)


n2 = int(input("Enter the limit list 2"))

for i in range(0,n2):
    value=int(input("Enter the value\n"))
    list2.append(value)


print(list1,list2)
                    
if( len(list1)==  len(list2)):
    print("Lists length are equal")

else:
     print("Oops Lists length are not equal")

if( sum(list1)==  sum(list2)):
    print("Lists sum are equal")

else:
     print("Oops Lists sum are not equal")     

list3 = [each for each in list1 if each in list2]

if( len(list3) > 0):
    print("Same elems of l1 and l2",list3)

else:
     print("Oops not found anything equal")     
    
