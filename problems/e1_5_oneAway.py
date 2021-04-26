# CTCI E1.5: There are three types of edits that can be performed on strings: insert, remove, replace a character. Given two strings, write a function to check if they are one edit away.
# Example:
# E1: "pale, ple --> True"
# E2: "pale, bake --> False"

def oneAway(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    diff = 0
    i = 0
    j = 0

    while (i < len(s1) and j < len(s2)):
        if s1[i] != s2[j]:
            diff += 1
            if diff > 1:
                return False
            if(len(s1) > len(s2)):
                i+=1
            elif len(s1) < len(s2):
                j+=1
        i+=1
        j+=1
    
    return diff <= 1


o1 = oneAway("pale", "ple")
print(o1)

o2 = oneAway("pale", "bake")
print(o2)