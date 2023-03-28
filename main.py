def count_anagrams(dictionary, query):
    """
    Counts the number of anagrams of each string in query that exist in dictionary.

    Parameters:
    dictionary (List[str]): The list of strings to search for anagrams.
    query (List[str]): The list of strings to find the anagrams of.

    Returns:
    List[int]: The list of integers representing the count of anagrams for each string in query.
    """
    # Create a dictionary to store the counts of characters in each string in the dictionary.
    dict_counts = {}
    for word in dictionary:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = ''.join(map(str, count))
        if key not in dict_counts:
            dict_counts[key] = 1
        else:
            dict_counts[key] += 1

    # Count the number of anagrams for each string in query using the dictionary.
    res = []
    for word in query:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = ''.join(map(str, count))
        if key not in dict_counts:
            res.append(0)
        else:
            res.append(dict_counts[key])
    return res
