import string,collections,decimal
fin = open("trainingdata.txt")

def predict(n,table):
    if n in table:
        print table[n]
        return
    if n >= 4.11 and n <= 11.72:
        print 8
        return
    charges = table.keys()
    charges.sort()
    for i in charges:
        if i > n:
            break
    high = i
    low = charges[charges.index(i)-1]
    value = ( ( (n-low)*table[high] ) + ( (high-n)*table[low] ) ) / ( (high-n) + (n-low) )  
    
    a = decimal.Decimal(str(value))
    print(round(a,2))

table2 = {}
def main():
    for line in fin:
        breakup = string.split(line,",")
        charge,laptop = float(breakup[0]),float(breakup[1]) 
        #print charge,laptop
        try :
            table2[charge] = laptop
        except KeyError:
            table2[charge] = 0
    #table = collections.OrderedDict(sorted(table2.items()))
    
    n = 0.09
    #n=input()
    predict(n,table2)
    
if __name__ == '__main__':
    main() 