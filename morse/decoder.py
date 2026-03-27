# morse/decoder.py

from morse.mapping import MORSE

# Ters mapping
REVERSE_MORSE = {value: key for key, value in MORSE.items()}


def decode_word(word):
    """
    Tek bir Morse kelimesini decode eder.
    Harfler boşluk ile ayrılmıştır.
    """
    chars = word.split()
    decoded_chars = []

    for c in chars:
        if c in REVERSE_MORSE:
            decoded_chars.append(REVERSE_MORSE[c])

    return "".join(decoded_chars)


def decode(morse_code):
    """
    Morse kodunu metne çevirir.
    Kelimeler | ile ayrılmıştır (boşluk olabilir olmayabilir)
    """
    # hem "|", hem " | " durumu için
    words = morse_code.strip().split("|")

    decoded_words = []

    for word in words:
        word = word.strip()  # boşluk temizle
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)


if __name__ == "__main__":
    # Example usage for one word
    example_word = "... --- ..."
    print(decode(example_word))  # SOS

    # Example usage for one sentence
    example_sentence = ".... . .-.. .-.. --- | .-- --- .-. .-.. -.."
    print(decode(example_sentence))  # HELLO WORLD
