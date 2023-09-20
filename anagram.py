# Check if two strings are anagrams of each other


from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

str1=input("enter a string 1:")

str2=input("entera string 2")

result = is_anagram(str1,str2)
print(result)  # False

