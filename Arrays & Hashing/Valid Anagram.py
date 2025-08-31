# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


s = "anagram"
t = "nagaram"


def anagram(s,t):
    return(sorted(s) == sorted(t))

print(anagram(s,t))
