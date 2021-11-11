# Function to find all subsequences of a string

def subsequencesOf(string):

    return helper("",string,[])

def helper(processed,unprocessed,ans):
    
    if unprocessed == "" :
        ans.append(processed)
        return
    ch = unprocessed[0]
    helper(ch + processed,unprocessed[1:], ans)
    helper(processed,unprocessed[1:], ans)

    return ans

#test code
s = "abc"
print(subsequencesOf(s))
