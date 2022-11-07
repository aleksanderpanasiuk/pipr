def delete_words(sentence, letter):
    fitting_words = []

    for word in sentence.split():
        if word.count(letter[0]) < letter[1]:
            fitting_words.append(word)

    return " ".join(fitting_words)


my_sentence = "Alice in wonderland went into a deep coma."
my_letter = 'e', 2

print(delete_words(my_sentence, my_letter))
