def prompt():
    print("String has all unique characters finder\n_____________________\n")

def bruteforce(string):
    for i in range(0,len(string)):
        for h in range(0,len(string)):
            if i!=h and string[i] == string[h]:
                return False
    return True
    
def bruteforcePlus(string):
    stringSorted = ''.join(sorted(string))
    for i in range(1,len(stringSorted)):
        if stringSorted[i-1] == stringSorted[i]:
            return False
    return True
        
def boolArray(string):
#Characters cannot be uniques if there is more character than the charset
    if len(string) > 128:
        return False
    charsetBool = [0] * 128
    for s in string:
        value = ord(s)
        if charsetBool[value] == True :
            return False
        charsetBool[value] = True
    return True

'''
a = 'ZENOVW'
b = sorted(a) # sorted returns a list
print b # ['E', 'N', 'O', 'V', 'W', 'Z']
c = ''.join(b) # so you can make it a string again using join
'''
        
def launch1DEfficientFinder(data):
    peak = get_1D_Efficient_Peak(data)
    print("Input tab : ", data, end ='\n')
    print("Peak : ", peak, end ='\n')
