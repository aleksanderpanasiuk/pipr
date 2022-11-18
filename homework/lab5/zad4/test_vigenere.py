from vigenere import encrypt_vigenere, decrypt_vigenere


def test_encrypt_vigenere_typical():
    key = "NT OJES TBARDZ OTAJN YTEKS"
    plain_text = "TO JEST BARDZO TAJNY TEKST"
    result = "GH XNWL UBRUCN HTJWL RXOCL"
    assert encrypt_vigenere(key, plain_text) == result


def test_encrypt_vigenere_typical2():
    key = "TAJNE"
    plain_text = "TO JEST BARDZO TAJNY TEKST"
    result = "MO SRWM BJEHSO CNNGY CROLT"
    assert encrypt_vigenere(key, plain_text) == result


def test_encrypt_vigenere_ZZZ():
    key = "AAAAA"
    plain_text = "ZZZZZZZZZZ"
    result = "ZZZZZZZZZZ"
    assert encrypt_vigenere(key, plain_text) == result


def test_decrypt_vigenere_typical():
    key = "NT OJES TBARDZ OTAJN YTEKS"
    cipher_text = "GH XNWL UBRUCN HTJWL RXOCL"
    result = "TO JEST BARDZO TAJNY TEKST"
    assert decrypt_vigenere(key, cipher_text) == result


def test_decrypt_vigenere_typical2():
    key = "TAJNE"
    cipher_text = "MO SRWM BJEHSO CNNGY CROLT"
    result = "TO JEST BARDZO TAJNY TEKST"
    assert decrypt_vigenere(key, cipher_text) == result


def test_decrypt_vigenere_ZZZ():
    key = "AAAAA"
    cipher_text = "ZZZZZZZZZZ"
    result = "ZZZZZZZZZZ"
    assert decrypt_vigenere(key, cipher_text) == result
