# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from itertools import islice
import io
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_keywords(content, heading):
    content_words = word_tokenize(content)

    content_without_stop_words = remove_stop_words(content_words)
    content_without_stop_words = remove_punctuations(content_without_stop_words)
    content_without_stop_words = remove_suffixes(content_without_stop_words)

    number_of_keywords = get_number_of_keywords(len(content_without_stop_words))

    if heading != None:

        heading_words = word_tokenize(heading)
        heading_without_stop_words = remove_stop_words(heading_words)
        heading_without_stop_words = remove_punctuations(heading_without_stop_words)
        heading_without_stop_words = remove_suffixes(heading_without_stop_words)

        return frequency_base_keyword_generating(content_without_stop_words, heading_without_stop_words,
                                                 number_of_keywords)
    else:
        return frequency_base_keyword_generating(content_without_stop_words, None, number_of_keywords)


def frequency_base_keyword_generating(content_word_list, heading_word_list, number_of_keywords):
    frequency = FreqDist(content_word_list)
    word_list_with_frequency = {}

    for word in content_word_list:

        weight = frequency[word]

        if heading_word_list != None:

            for heading_word in heading_word_list:
                if word == heading_word:
                    weight = weight + 2

        word_list_with_frequency[word] = weight

    # sorted_word_list = [(k, word_list_with_frequency[k]) for k in
    #                     sorted(word_list_with_frequency, key=word_list_with_frequency.get, reverse=True)]
    sorted_word_list = [k for k in
                        sorted(word_list_with_frequency, key=word_list_with_frequency.get, reverse=True)]

    key_words = list(islice(sorted_word_list, number_of_keywords))
    return key_words


def get_number_of_keywords(content_word_length):
    if content_word_length < 50:
        number_of_keywords = 3
    else:
        if content_word_length < 100:
            number_of_keywords = 4
        else:
            number_of_keywords = (content_word_length * 5) / 100

    return number_of_keywords


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
    punc_list = [".", ",", "?", "!", ";", ":", "-", "(", ")", "[", "]", "{", "}", "'", '"', "..."]

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
                    word = word[:len(word) - len(suffix)]
                    break

            non_suffix_word_list.append(word)

    for non_suffix_word in non_suffix_word_list:
        if len(non_suffix_word) <= 2:
            non_suffix_word_list.remove(non_suffix_word)

    return non_suffix_word_list


def has_suffix(text, suffix):
    if text.endswith(suffix):
        return True
    else:
        return False

# def strip_left(text, prefix):
#     if not text.startswith(prefix):
#         return text
#     # else
#     return text[len(prefix):]
