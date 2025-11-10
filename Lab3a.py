def countCharacters(sen):
    word_count = len(sen.split())
    digit_count = sum(1 for char in sen if char.isdigit())
    upper_count = sum(1 for char in sen if char.isupper())
    lower_count = sum(1 for char in sen if char.islower())
    return word_count, digit_count, upper_count, lower_count

sentence = input("Enter a sentence: ")
word_count, digit_count, upper_count, lower_count = countCharacters(sentence)

print(f"Number of words: {word_count}")
print(f"Number of digits: {digit_count}")
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")