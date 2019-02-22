# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize
from itertools import islice

from word_filter import get_filtered_word_list2
import config

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_content_summary_final(content, heading, keywords):
    final_summary = ''
    sent_tokenize_list = sent_tokenize(content)
    total_num_of_sentences = len(sent_tokenize_list)

    sentences_with_weight = {}

    for sentence in sent_tokenize_list:
        sentence_location = (sent_tokenize_list.index(sentence) + 1)
        keyword_scoring = get_keyword_score(keywords, sentence)
        location_scoring = get_location_score(sentence_location, total_num_of_sentences) / 5
        title_scoring = get_title_score(heading, sentence)

        total_score = ((config.KEYWORD_VALUE * keyword_scoring) + (config.LOCATION_VALUE * location_scoring) + (
                config.TITLE_VALUE * title_scoring)) / (config.KEYWORD_VALUE + config.TITLE_VALUE + config.LOCATION_VALUE)
        sentences_with_weight[sentence] = total_score

        # print total_score

    sorted_sentence_list = [k for k in
                            sorted(sentences_with_weight, key=sentences_with_weight.get, reverse=True)]
    try:
        highest_weight = sentences_with_weight[sorted_sentence_list.__getitem__(0)]
    except:
        print "error"

    # remove sentences with weight that are lower than 40% of highest weighted sentence
    for sent in sorted_sentence_list:
        if (sentences_with_weight[sent] / highest_weight) < 0.4:
            sorted_sentence_list.remove(sent)

    if len(sorted_sentence_list) > 3:
        number_of_sentences_in_summary = get_number_of_sentences(total_num_of_sentences)
    else:
        number_of_sentences_in_summary = 1

    # print number_of_sentences_in_summary

    summary_sentences = list(islice(sorted_sentence_list, number_of_sentences_in_summary))

    # try:
    #     if sent_tokenize_list[0] not in summary_sentences:
    #         summary_sentences.pop()
    #         summary_sentences.append(sent_tokenize_list[0])
    # except:
    #     print 'error'

    for sentence in sent_tokenize_list:
        if sentence in summary_sentences:
            final_summary = final_summary + sentence

    return final_summary


def get_location_score(sentence_location, total_num_of_sentences):
    value = 0.0
    if total_num_of_sentences > 1:
        if sentence_location < ((total_num_of_sentences + 1) / 2):
            value = 1.0 - ((2.0 / (total_num_of_sentences - 1)) * (sentence_location - 1))
        elif sentence_location > ((total_num_of_sentences + 1) / 2):
            value = 1.0 - ((2.0 / (total_num_of_sentences - 1)) * (total_num_of_sentences - sentence_location))
        elif sentence_location == ((total_num_of_sentences + 1) / 2):
            value = 0.1

    return value


def get_keyword_score(keywords, sentence):
    word_list = get_filtered_word_list2(sentence)
    sentence_keyword_score = 0.0
    if len(word_list) > 0:
        for word in word_list:
            if word in keywords:
                sentence_keyword_score = sentence_keyword_score + keywords[word]

        return sentence_keyword_score / len(word_list)
    else:
        return 0


def get_title_score(heading, sentence):
    heading_words = get_filtered_word_list2(heading)
    sentence_words = get_filtered_word_list2(sentence)
    number_of_title_words = 0.0
    if len(sentence_words) > 0:
        for word in sentence_words:
            if word in heading_words:
                number_of_title_words = number_of_title_words + 1.0
        return number_of_title_words / len(sentence_words)
    else:
        return 0


# def get_keyword_percentage_of_sentence(keywords, sentence):
#
#     non_suffix_word_list = get_filtered_word_list2(sentence)
#     total_words = len(non_suffix_word_list)
#     number_of_keywords = 0.0
#
#     for word in non_suffix_word_list:
#         if word in keywords:
#             number_of_keywords += 1.0
#
#     try:
#         keyword_probability = (number_of_keywords / total_words * 100)
#     except:
#         keyword_probability = 0
#
#     return keyword_probability


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
                return (config.SENTENCE_PERCENTAGE / 100) * sentence_length
