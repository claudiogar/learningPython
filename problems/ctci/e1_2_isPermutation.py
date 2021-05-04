# CTCI 1.2: Check permutations
# Given two strings, write a method to decide if one is a permutation of the other.

def isPermutation(s1:str, s2:str)-> bool:
    l1 = len(s1)
    l2 = len(s2)

    if l1 != l2: return False

    dict = {}

    # O(n)

    for c in s1:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    
    for c in s2:
        if c in dict:
            dict[c] -= 1
        else:
            dict[c] = 1

    for key in dict:
        if dict[key] != 0: return False
    

    return True


