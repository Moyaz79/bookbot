def word_count(input_string):
    return len(input_string.split())

def char_count(input_string):
    text = input_string.lower()
    character_count = {}
    for char in text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1 
    return character_count

def sorting(item):
    return item[1]
