# CTCI E1.4: Palindrome permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same fowards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionaryt words. You can ignore casing and non-letter characters.
# Example:
# INPUT: "tact coa"
# OUTPUT: True (permutations: "taco cat", "atco cta", etc.)

def isPalindromePermuation(s:str) -> bool:
    chars = {}
    length = 0

    for i in range(0, len(s)):
        if shouldIgnore(s[i]):
            continue
        else:
            c = s[i].lower()
            length += 1
            if(c in chars):
                chars[c] = not chars[c]
            else:
                chars[c] = True
    
    odds = 0
    for c in chars:
        if chars[c]:
            odds += 1

    return odds == 1

def shouldIgnore(char:chr) -> bool:
    return char == ' '


e1 = isPalindromePermuation("Tact Coa")
print(e1)

e2 = isPalindromePermuation("a")
print(e2)

e3 = isPalindromePermuation("ab")
print(e3)
