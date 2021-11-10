#function to skip a specific character from a string
def skip(string,character):
    
    if string == "" :
        return ""
    if string[0] != character:
        return string[0] + skip(string[1:],character)
    else:
        return skip(string[1:],character)     
    
    
    
#test code
s = "baccabd"
print(skip(s,"a"))