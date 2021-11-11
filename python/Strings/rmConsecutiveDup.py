# Recursive function to remove consecutive duplicates from a string

def removeDup(strn):
    if strn == "" :
        return ""

    if len(strn) == 1:
        return strn    
    
    if strn[0] == strn[1] :
        return removeDup(strn[1:])
    else:
        return strn[0] + removeDup(strn[1:])

#test code
s = "aabbcskuhfs"
print(removeDup(s))
