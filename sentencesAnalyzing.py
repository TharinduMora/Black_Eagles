# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from itertools import islice

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_content_summary(content, keywords):

    final_summary = ''
    sent_tokenize_list = sent_tokenize(content)
    number_of_sentences_in_summary = get_number_of_sentences(len(sent_tokenize_list))
    sentences_with_probability = {}

    for sentence in sent_tokenize_list:
        keyword_probability = get_keyword_probability_of_sentence(keywords, sentence)
        sentences_with_probability[sentence] = keyword_probability

    sorted_sentence_list = [k for k in
                            sorted(sentences_with_probability, key=sentences_with_probability.get, reverse=True)]

    summary_sentences = list(islice(sorted_sentence_list, number_of_sentences_in_summary))

    for sentence in sent_tokenize_list:
        if sentence in summary_sentences:
            final_summary = final_summary + sentence

    return final_summary


def get_keyword_probability_of_sentence(keywords, sentence):
    word_list = word_tokenize(sentence)
    total_words = len(word_list)
    number_of_keywords = 0.0

    for word in word_list:
        if word in keywords:
            number_of_keywords += 1.0

    keyword_probability = (number_of_keywords / total_words * 100)

    return keyword_probability


def get_number_of_sentences(sentence_length):
    if sentence_length <= 2:
        return 1
    else:
        if sentence_length < 7:
            return 2
        else:
            if sentence_length < 10:
                return 3
            else:
                return 30 / 100 * sentence_length
