import difflib

def string_similarity(str1, str2):
    result = difflib.SequenceMatcher(None, str1.lower(), str2.lower())
    return result.ratio()

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Original strings:")
print(str1)
print(str2)

print("Similarity between the two is:", string_similarity(str1, str2))