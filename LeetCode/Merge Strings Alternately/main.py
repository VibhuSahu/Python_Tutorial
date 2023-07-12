'''
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

def mergeStringsAlternately(word1, word2):

    # Putting value into list
    listWord1 = list(word1)
    listWord2 = list(word2)

    # length of list
    lengthWord1 = len(listWord1)
    lengthWord2 = len(listWord2)

    # (Blank variable) for add element of list in this
    Word = ''

    # While loop help you to add elements
    count = 0
    while True:
        if (((lengthWord1 - count) > 0) and ((lengthWord2 - count) > 0)):
            Word = Word + listWord1[count] + listWord2[count]
        elif (((lengthWord1 - count) > 0) or ((lengthWord2 - count) > 0)):
            if ((lengthWord1 > lengthWord2)):
                Word += listWord1[count]
            else:
                Word += listWord2[count]
        else:
            break

        # Alternating the count variable
        count += 1
    return Word


print(mergeStringsAlternately("abcde","pqr"))