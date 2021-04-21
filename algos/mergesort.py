def mergesort(array, i , j):
    if i >= j: return array[i:j+1]

    mid = int((i+j)/2)
    a = mergesort(array, i, mid)
    b = mergesort(array,mid+1, j)

    return merge(a,b)

def merge(a, b):
    length = len(a)+len(b)
    output = [None] * length

    i = 0
    j = 0
    z = 0
    while i < len(a) and j < len(b):
        if b[j] < a[i]:
            output[z] = b[j]
            j += 1
        else:
            output[z] = a[i]
            i += 1
        z += 1
    
    while i < len(a):
        output[z] = a[i]
        z += 1
        i += 1
    while j < len(b):
        output[z] = b[j]
        z += 1
        j += 1
    
    return output

