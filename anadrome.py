import math
inp = input("\nEnter string : ")
word = list(inp)
c=0
l = len(word)
for i in range(l):
    for j in range(i+1,l):
        if(word[i] == word[j]):
            c+=1


if(c >= math.floor(l/2)):
    print("its an anadrome")
else :
    print("it's not an anadrome")
