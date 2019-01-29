# -*- coding: utf-8 -*-
from keywordExtraction import get_keywords
from sentencesAnalyzing import get_content_summary
from TFIDF_Weighting import tf_idf_base_weighting, get_document_keywords

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def create_summary(heading, content):
    content = content.replace('COLOMBO (News 1st) :', '')
    content = content.replace('COLOMBO (News 1st) – ', '')
    content = content.replace('COLOMBO', '')
    content = content.replace('(News 1st):', '')
    content = content.replace('(News 1st)-', '')

    # keywords = get_keywords(content, heading)
    keywords = get_document_keywords(content)
    # for k in keywords:
    #     print(k)
    # print ()
    summary = get_content_summary(content, keywords)

    return summary


def get_weighted_words(content):
    doc = tf_idf_base_weighting(content)
    return doc


def get_keywords(content):
    doc = get_document_keywords(content)
    return doc
