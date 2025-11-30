def num_words(text):
    words = text.split()
    return len(words)


def num_characters(text):
    lower = text.lower()
    char_count = {}
    for char in lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]


def sorted_chars(num_chars):
    sorted_list = []
    for char in num_chars:
        if char.isalpha():
            num = num_chars[char]
            temp_dict = {"char": char, "num": num}
            sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
