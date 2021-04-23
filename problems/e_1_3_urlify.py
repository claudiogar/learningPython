# CTCI E1.3: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.dict
# Example:
# INPUT: "Mr John Smith    ", 13 
# OUTPUT: Mr%20John%20Smith"

def urlify(s:str, n:int) -> str:
    i = 0
    # O(n^2)
    for i in range(0, n):
        if s[i] != ' ':
            continue
        else:
            s = shift(list(s),i+1, n+1)
            n += 2
            s[i] = '%'
            s[i+1] = '2'
            s[i+2] = '0'
            i += 1
    return s


# O(n)
def shift(s:str, i:int, n:int) -> str:
    for j in range(0, n-i):
        s[n-j] = s[n-j-2]
    return s


print(urlify("Mr John Smith    ", 13))