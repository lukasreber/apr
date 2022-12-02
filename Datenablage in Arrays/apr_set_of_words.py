punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789—“”‘’'
punctuation_translation = str.maketrans(punctuation, ' ' * len(punctuation))


def words_from_file(file_name, encoding=None):
    with open(file_name, encoding=encoding) as f:
        for line in f:
            for word in line.lower().translate(punctuation_translation).split():
                yield word


def build_word_list(words):
    word_list = []
    for word in words:
        if word not in word_list:
            word_list.append(word)
    return word_list


def build_word_set(words):
    word_set = {word for word in words}
    return list(word_set)


def analyse_file(collecting_func, file_name, encoding=None):
    print('\ntesting', collecting_func.__name__)
    words = collecting_func(words_from_file(file_name, encoding=encoding))
    print(len(words))
    print(words[:10])


def main():
    file_name, enc = './data/shakespeare.txt', 'utf8'
    analyse_file(build_word_set, file_name, encoding=enc)
    analyse_file(build_word_list, file_name, encoding=enc)


if __name__ == '__main__':
    main()
