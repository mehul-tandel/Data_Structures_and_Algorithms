def maxProduct(arr):
    n = len(arr)

    maxVal = minVal = maxProd = arr[0]
    
    for i in range(1,n):
        if arr[i]<0:
            maxVal,minVal = minVal,maxVal
            
        maxVal = max(arr[i],arr[i]*maxVal)
        minVal = min(arr[i],arr[i]*minVal)
        maxProd = max(maxProd,maxVal)
        
    return maxProd

# test code
a = [9,0,8,-1,-2,-2,6]
print(maxProduct(a))