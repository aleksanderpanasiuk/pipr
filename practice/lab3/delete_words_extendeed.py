def delete_words_extended(sentence, letters):
    fitting_words = []

    for word in sentence.split():
        fits = letters_in_word(word, letters)

        if fits:
            fitting_words.append(word)

    return " ".join(fitting_words)


def letters_in_word(word, letters):
    for letter in letters:
        if word.count(letter[0]) >= letter[1]:
            return False

    return True


my_sentence = "I literally can't deal with this drama right now."
my_letters = [('a', 2), ('l', 3)]

print(delete_words_extended(my_sentence, my_letters))
