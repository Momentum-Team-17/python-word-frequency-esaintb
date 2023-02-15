import string

STOP_WORDS = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for',
              'from', 'has', 'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that',
              'the', 'to', 'were', 'will', 'with', 'if', 'we', 'she']


def remove_punctuation(words):
    # for char in PUNCTUATION:
    stripped_file = words.translate(str.maketrans('', '', string.punctuation))
    return stripped_file


# 4. remove "stop words" - words used so frequently we ignore
def remove_stop_words(word_list):
    cleaned_list = []
    for word in word_list:
        if word not in STOP_WORDS:
            cleaned_list.append(word)
    return cleaned_list


# 1. use 'open' to read a text file
def open_file(file):
    with open(file) as opened_file:
        read_file = opened_file.read()
        # 2. remove punctuation
        # 3. normalize all words to lowercase
    stripped_file = remove_punctuation(read_file).lower()
    word_list = stripped_file.split()
    # calling the removal of stop words
    cleaned_list = remove_stop_words(word_list)
    print(cleaned_list)
    return cleaned_list


# 5. count frequency of words in a file
# loop through the list of words, and updated the dictionary to indicate how many of each we have
def print_word_freq(file):
    words_to_count = open_file(file)
    word_count = {
        'new': words_to_count.count('new')
    }
    for word in words_to_count:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)


# 6. display a count in the console in descending frequency


# 7. turn numbers into *

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
