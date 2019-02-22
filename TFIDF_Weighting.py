# -*- coding: utf-8 -*-
from word_filter import get_filtered_word_list2
from DB_Configurations.db_connection import get_word_probability_list
from itertools import islice
from math import log
from nltk.probability import FreqDist
import sys
import config

reload(sys)
sys.setdefaultencoding('utf8')


def tf_idf_base_weighting(content):
    word_list = get_filtered_word_list2(content)
    word_count = len(word_list)
    frequency = FreqDist(word_list)

    sorted_word_list = [k for k in
                        sorted(frequency, key=frequency.get, reverse=True)]

    inverse_document_frequency_list = get_word_probability_list()

    word_list_with_frequency = {}
    weighted_word_list = []

    for obj in inverse_document_frequency_list:
        word_list_with_frequency[obj['word']] = obj['probability']

    for word in sorted_word_list:

        if word in word_list_with_frequency:
            tf_value = ((frequency[word] * 0.5) / word_count) + 0.5
            idf_value = log((1.0 / word_list_with_frequency[word]), 10)
            tf_idf_value = tf_value * idf_value
            weighted_word_list.append({"word": word, "weight": tf_idf_value})
            # print "word =",word,"-- weight = ",tf_idf_value

    weighted_word_list = sorted(weighted_word_list, reverse=True, key=sort_by_weight)

    return weighted_word_list


def sort_by_weight(e):
    return e['weight']


def get_document_keywords(content):
    weighted_word_list = tf_idf_base_weighting(content)
    distinct_word_count = len(weighted_word_list)
    number_of_keywords = get_number_of_keywords(distinct_word_count)

    sliced_words = list(islice(weighted_word_list, number_of_keywords))

    keywords = []
    keywords_as_collection = {}
    for word in sliced_words:
        keywords.append(word['word'])
        keywords_as_collection[word['word']] = word['weight']
        # print word , keywords_as_collection[word]

    return keywords_as_collection


# def get_number_of_keywords(word_count):
#     count = (get_number_of_keywords(word_count) * 5) / 100
#     return count


def get_number_of_keywords(content_word_length):
    if content_word_length < 50:
        number_of_keywords = 5
    else:
        if content_word_length < 100:
            number_of_keywords = 8
        else:
            number_of_keywords = (content_word_length * config.KEYWORD_PERCENTAGE) / 100

    return number_of_keywords
