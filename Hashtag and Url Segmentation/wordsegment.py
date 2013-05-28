"""
 * wordsegment.py
 *
 * Author: Shyam Shankar <syamsankar91@gmail.com>
 * Licensed under GPL Version 3
 *
 * It segments hashtags and urls into meaningful words
"""

fin = open("words.txt")
import re

def readwords():
    wset = []
    for word in fin:
        wset.append(word.replace("\n","").lower() )
    return wset

def validsegments(string,wset):
    # Sort wset in decreasing string order
    wset.sort(key=len, reverse=True)
    result = tokenize(string, wset, "")
    if result:
        result.pop() # Remove the empty string token
        result.reverse()
        return result
    else:
        return None

def tokenize(string, wset, token):
    # Remove token
    string = string.replace(token, '', 1)
    # 
    if string == "":
        return [token]
    # Find all possible prefixes
    for pref in wset:
        if string.startswith(pref):
            res = tokenize(string, wset, pref)
            if res:
                res.append(token)
                return res
    # Not possible
    return False

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def main():
    wset = readwords()

    n=input()
    for k in xrange(n):
        text = raw_input()

        if text[0] == '#':
            pattern = r'(#)([\w.]+)'

        else:
            #pattern = r'(www.)?([\w.]+).\D+'
            pattern = r'(www.)?(\w+).'

        m = re.match(pattern,text)
        if m == None:
            print text
            continue
        segmnt = m.group(2)
        #print segmnt,"   ",text            
        final = re.findall(r'[\d.]+|\D+', segmnt)
        #print final,text
        
        valid = []
        breakflag = False
        for str1 in final:
            if isFloat(str1):
                valid.append(str1)
            else:
                vlist = validsegments(str1,wset)
                if vlist == None or len(vlist) == len(str1):
                    print segmnt
                    breakflag = True
                    break
                else:
                    map(lambda x:valid.append(x) , vlist)    
        
        if breakflag == False:
            print " ".join(valid)
            
if __name__ == '__main__':
    main() 