# - *- coding: utf- 8 - *-
from nltk.tokenize import word_tokenize
import io
import re


# return only distinct words
def get_filtered_word_list(content):
    content_words = word_tokenize(content)

    word_list = remove_stop_words(content_words)
    word_list = remove_punctuations(word_list)
    word_list = remove_suffixes(word_list)
    word_list = list(set(word_list))
    return word_list


# return words with multiple occurrences
def get_filtered_word_list2(content):
    content_words = word_tokenize(content)

    word_list = remove_stop_words(content_words)
    word_list = remove_punctuations(word_list)
    word_list = remove_suffixes(word_list)
    # word_list = list(set(word_list))
    return word_list


def remove_stop_words(content_word_list):
    with io.open("./Sinhala Functional Words/Stop Words.txt", 'r', encoding='utf8') as outfile:
        x = outfile.read()
        stop_words = word_tokenize(x)
        word_list_without_stop_words = []

        for word in content_word_list:
            if word not in stop_words:
                word_list_without_stop_words.append(word)

        return word_list_without_stop_words


def remove_punctuations(words):
    word_list = []
    punc_list = [".", ",", "?", "!", ";", ":", "-", "(", ")", "[", "]", "{", "}", "'", '"', "...", "`"]

    for n in words:
        if n not in punc_list:
            x = re.match("[0-9]", n)
            if x == None:
                word_list.append(n)

    return word_list


def remove_suffixes(word_list):
    with io.open("./Sinhala Functional Words/Suffixes-413.txt", 'r', encoding='utf8') as outfile:
        x = outfile.read()
        suffix_list = word_tokenize(x)

    non_suffix_word_list = []
    for word in word_list:

        if len(word) > 3:
            for suffix in suffix_list:

                if has_suffix(word, suffix):
                    if len(word[:len(word) - len(suffix)]) > 3:
                        word = word[:len(word) - len(suffix)]

                    break

            non_suffix_word_list.append(word)

        else:
            if len(word) > 1:
                non_suffix_word_list.append(word)

    # for non_suffix_word in non_suffix_word_list:
    #     if len(non_suffix_word) <= 2:
    #         non_suffix_word_list.remove(non_suffix_word)

    return non_suffix_word_list


def has_suffix(text, suffix):
    if text.endswith(suffix):
        return True
    else:
        return False

# def remove_non_ascii(list):
#     # for word in list:
#     #     word = re.sub(r'[^\x00-\x7F]+', ' ', word)
#
#     # onlyascii = ''.join([s for s in list if ord(s)<127])
#     # print onlyascii
#     for word in list:
#         word = word.decode('utf-8','ignore').encode("utf-8")
#         print word
#
#     return list
