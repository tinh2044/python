def anagrams(word, words):
    
    return [item for item in words if sorted(item) == sorted(word)]
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))