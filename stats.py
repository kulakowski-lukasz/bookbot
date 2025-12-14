def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def sorted_list(chars):
    sorted_chars = []
    for char in chars:
        if char.isalpha():
            char_dict = {"char": char, "num": chars[char]}
            sorted_chars.append(char_dict)

    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
