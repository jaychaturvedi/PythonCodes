# import sys
    # sys.stdout.flush()
'''Welcome to MyDictionary
        @author : JayChaturvedi @Git : KILLBEE'''
import json
import time
from difflib import get_close_matches
from random import uniform
data = json.load(open("data.json"))                                             #loads data.json file which contains all dictionary keys and values

for i in __doc__:                                                               #prints documentstring of program
    print(i,end=" ",flush = True)
    time.sleep(0.03)

word = input("\nSearch for meaning : ")                                         #takes input from the user


def Search(word):                                                               #Search for word meaning in the data.json file
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))> 0:                          #get_close_matches() search for similar word in data.json
        word = get_close_matches(word ,data.keys())[0]
        yn = input("did you mean %s ? Press Y if Yes or N for No:  " %word ).upper()
        if yn == 'Y' :
            return (data[word])
        elif yn == 'N':
            return("Sorry word doesn't exist, Please double check it")
        else:
            return("We didn't understand your entry")
    else :
        return("Sorry word doesn't exist, Please double check it")


output = Search(word.lower())
if type(output) == list:                                                        #checks if word have more than one meaning
    for i in output :
        print(i,end='\n')
else:
    print(output)
