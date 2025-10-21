string = input("Enter the string");
len = len(string)
first = string[0]
last = string[len-1]
modStr= last + string[1:len-2] + first
print("Modded string",modStr)
