def alphabet_position(letter):
    letter = letter.lower()
    every_letter = "abcdefghijklmnopqrstuvwxyz"
    ix = 0
    for i in every_letter:
        if i != letter:
            ix += 1
        else:
            return ix

def rotate_character(char, rot):
    import string
    temp_char = char.lower()
    every_letter = "abcdefghijklmnopqrstuvwxyz"
    ix = alphabet_position(temp_char)
    new_ix = ix + rot
    new_ix = new_ix % 26
    new_char = every_letter[new_ix]
    if char in string.ascii_lowercase:
        return new_char.lower()
    elif char in string.ascii_uppercase:
        return new_char.upper()
    else:
        return char


def encrypt(text, rot):
    encrypted_text = ""
    full_letter_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in text:
        if i in full_letter_string:
            a = rotate_character(i, rot)
            encrypted_text = encrypted_text + a
        else:
            encrypted_text = encrypted_text + i
    return encrypted_text
