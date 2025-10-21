string = input("Enter the string")
first = string[0]
modStr = first+string[1:].replace(first,"$")
print("Modified String",modStr)              
              
