# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def summary(heading, content):
    # print "Heading = ", heading
    sent_tokenize_list = sent_tokenize(content)
    length = len(sent_tokenize_list)
    final_summary = ''
    i = 0
    for sentence in sent_tokenize_list:
        sentence = sentence.replace('COLOMBO (News 1st) : ', '')
        sentence = sentence.replace('COLOMBO (News 1st) – ', '')
        if i == 0:
            final_summary = final_summary + sentence
        if i == length - 1:
            final_summary = final_summary + sentence
        i += 1

    return final_summary
