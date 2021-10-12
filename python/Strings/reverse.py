#function to reverse a string
def reverse(string):
    ans = ""
    for s in string:
        ans = s + ans
    return ans

#test code
a = "abcde"
a = reverse(a)
print(a)