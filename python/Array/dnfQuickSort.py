# Dutch National Flag Algorithm

def dnfSort(arr, pivot_index):
    
    pivot = arr[pivot_index]
    smaller, equal, larger = 0, 0, len(arr)

    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1

        elif arr[equal] == pivot:
            equal +=1
        
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]




