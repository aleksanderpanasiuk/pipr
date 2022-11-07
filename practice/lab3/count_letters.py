def count_letters(word):
    letters = {}

    for letter in word:
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters


my_word = "kukułka"

print(count_letters(my_word))
