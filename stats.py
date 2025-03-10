def get_num_words(text):
    return len(text.split())

def get_character_freq(text):
    freq = {}
    for character in text:
        lower_character = character.lower()
        if lower_character not in freq:
            freq[lower_character] = 1
        else:
            freq[lower_character] += 1
    return freq

def get_sorted_character_freq( freq):
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq
