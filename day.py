def find_substring_with_most_vowels(s, k):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    max_vowel_count = 0
    max_vowel_substring = ""
    vowel_count = 0
    for i in range(len(s) - k + 1):
        if i == 0:
            for j in range(k):
                if s[j] in vowels:
                    vowel_count += 1
        else:
            if s[i-1] in vowels:
                vowel_count -= 1
            if s[i+k-1] in vowels:
                vowel_count += 1
        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
            max_vowel_substring = s[i:i+k]
    if max_vowel_count == 0:
        return "Not found!"
    else:
        return max_vowel_substring
