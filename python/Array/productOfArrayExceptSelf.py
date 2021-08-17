

def productOfArrayExceptSelf(arr,n):

    m = 10**9 + 7
    productOfAll = 1
    count = 0
    for i in arr:
        if i == 0:
            count += 1
        if i != 0:
            productOfAll = (productOfAll * i)%m
    
    if count > 1:
        return [0]*n
    product = [productOfAll]*n

    for i in range(n):
        if count == 1:
            if arr[i] != 0 :
                product[i] = 0
        else:
            product[i] = product[i]//arr[i]

    return product