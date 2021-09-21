# Sieve of Eratothenes
# Function to find all prime numbers from 0 to n

def seiveOfEratothenes(n):

    arr = [True for i in range(n+1)]
    arr[0] = False
    arr[1] = False

    i = 2
    while i*i <= n:
        
        for j in range(i*2,n+1,i): 
            arr[j] = False
        i += 1

    return arr

# test code
# print(seiveOfEratothenes(20))

def gcd(a,b):
    
    if b == 0:
        return a
    gcd(b, a%b)