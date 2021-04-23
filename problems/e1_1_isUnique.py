# Excercise 1.1 from Cracking the coding interview
# Problem: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def isUnique(s:str) -> bool:
    initialLength = len(s)

    # if there are more chars than the whole ASCII alphabet, there must be a repetition
    if len(initialLength > 128):
        return False

    # O(n^2): without sorting and additional data structures, we can do the below
    # (or anything similar, like two nested loops).
    # If we could at least do sorting, this could become O(nlogn)
    while initialLength > 0:
        c = s[0]
        s = s.replace(c, '')
        if(len(s) != initialLength - 1):
            return False
        initialLength = len(s)
    return True


e0 = ''
e1 = 'aabbcc'
e2 = 'ababc'
e3 = 'abcd'

print(isUnique(e0))
print(isUnique(e1))
print(isUnique(e2))
print(isUnique(e3))


