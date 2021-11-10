# Function to skip specific substring from a string
def skipString(string,word):
    n = len(word)
    if string == "" :
        return ""
    if string[:n] != word :
        return string[0] + skipString(string[1:],word)
    else:
        return skipString(string[n-1 :],word)

#test code
s = "oifjapplekdfhappl"
print(skipString(s,"apple"))