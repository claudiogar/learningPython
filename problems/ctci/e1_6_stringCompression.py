#CTCI E1.6: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compress(s:str) -> str:
    output = []

    i = 0
    while i < len(s):
        c = s[i]
        count = 1
        if i < len(s) - 1:
            j = i+1
            while j < len(s):
                if s[j] == c:
                    count += 1
                else:
                    break
                j += 1
        
        output.append(c)
        output.append(str(count))

        i = j 
    
    if len(output) == len(s):
        return s
    return output


input = "aabcccccaaa"

o = compress(input)
print(''.join(o))
