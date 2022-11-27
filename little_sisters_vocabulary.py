"""Functions for creating, transforming, and adding prefixes to strings.
source: https://exercism.org/tracks/python/exercises/little-sisters-vocab
"""


def add_prefix_un(word):
    return f"un{word}"


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return prefix + " :: " + " :: ".join([prefix + word for word in vocab_words[1:]])


def remove_suffix_ness(word):
    origin = list(word)[:-4]
    if origin[-1] == 'i':
        origin[-1] = 'y'
    return ''.join(origin)


def adjective_to_verb(sentence, index):
    phrase = sentence.split()
    word = phrase[index].strip(".")
    return f"{word}en"

