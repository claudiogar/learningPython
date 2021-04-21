import random


###################
# Complexity:
# Time:
#   Worst case (pivot is consistently the greatest element): O(Nˆ2)
#   Average case: we halve the array with each call of quicksort O(N*logN)

##################

def quicksort(array):
    quicksort_inplace(array, 0, len(array)-1)

def quicksort_inplace(array, low, high):
    if(low < high):
        pivotIndex = partition(array, low, high)
        quicksort_inplace(array, low, pivotIndex-1)
        quicksort_inplace(array, pivotIndex+1, high)

def partition(array, low, high):
    i = low - 1
    j = low
    pivot = array[high]

    while j < high:
        if array[j] < pivot:
            i = i + 1
            swap(array, i, j)
        j = j+1
    swap(array, i+1, high)
    return i+1

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    pass