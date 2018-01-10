import json
from difflib import SequenceMatcher,get_close_matches

data = json.load(open('data.json'))
cn=0
def dictionary(key):
    return str(data[key])

def input_word():
    key=input("Enter a word to search:")
    try:
        key=key.lower()
        validate(key)
#        print(dictionary(key))
    except KeyError:
        print("Invalid word")

def validate(key):
    global cn
    if key not in data.keys():
            key=''.join(get_close_matches(key,data.keys(),n=1))
            print("Do you mean '"+key+"' instead??"+'\n'+'Enter Y for yes'+' or'+' Enter N for No')
            i=input("Enter your response:")
            i=i.lower()
            if i == 'y':
                print(dictionary(key))
            elif i == 'n':
                cn+=1
                if cn > 3:
                    key1=get_close_matches(key,data.keys(),n=4)
                    print("Are you looking for '"+key1[0]+"' or '"+key1[1]+"' or '"+key1[2]+"' or '"+key1[3]+"' instead??"+'\n'+"Enter '1' for 1st word"+'\n'+' or'+" Enter '2' for 2nd word"+'\n'+' or'+" Enter '3' for 3rd word"+'\n'+' or'+"Enter '4' for 4th word")
                    j=int(input("Enter your choice: "))
                    if j == 1:
                        key=key1[0]
                        print("You selected '"+key+"'")
                        print(dictionary(key))
                    elif j == 2:
                        key=key1[1]
                        print("You selected '"+key+"'")
                        print(dictionary(key))
                    elif j == 3:
                        key=key1[2]
                        print("You selected '"+key+"'")
                        print(dictionary(key))
                    elif j == 4:
                        key=key1[3]
                        print("You selected '"+key+"'")
                        print(dictionary(key))
                    else:
                        print("Sorry !!Your word not in my dictionary ")
                        exit()
                        
                else:
                    input_word()
                
                    
            else:
                print("Incorrect response, please enter correct response")
                
    else:
        print(dictionary(key))
input_word()