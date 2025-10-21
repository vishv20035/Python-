string1 = input("Enter the 1st string")
string2 = input("Enter the 2nd string")

modStr = string2[0]+string1[1:] + "" + string1[0]+string2[1:]
print("Modified String",modStr)              
              
