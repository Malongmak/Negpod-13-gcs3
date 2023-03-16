word = input("Enter a word: ").lower()
vowels = "aeiouy"
i = 0
while i < len(word):
    if word[i] not in vowels:
        print(word[i])
    i += 1
