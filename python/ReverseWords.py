def reverseWord(lstr, i, j):
    """
    This function reverse the word in a list between i and j
    """
    while(i < j):
        lstr[i], lstr[j] = lstr[j], lstr[i]
        i += 1
        j -= 1   
        
def reverseWords(input_str):
    """
    This function reverse the alphabatic words in a given string.
    It keeps the position of non-alphabetic character as it is.
    Example: input: Hello World, How are you?
             output: olleH dlroW, woH era uoy?
    """
    lstr = list(input_str)
    m = -1
    n = -1
    for i in range(len(lstr)):
        if lstr[i].isalpha():
            if m == -1:
                m = i
        else:
            if m > -1:
                n = i - 1
                reverseWord(lstr, m, n)
                m = -1
                n = -1
    if m > -1:
        n = len(lstr) - 1
        reverseWord(lstr, m, n)

    return ''.join(lstr)


print reverseWords('Hello World, How are you?')
