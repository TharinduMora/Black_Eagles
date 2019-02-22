# -*- coding: utf-8 -*-
from keywordExtraction import get_keywords
from sentencesAnalyzing import get_content_summary
from sentenceFilter import get_content_summary_final
from TFIDF_Weighting import tf_idf_base_weighting, get_document_keywords

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def create_summary(heading, content):
    keywords = get_document_keywords(content)
    # summary = get_content_summary(content, keywords)
    summary = get_content_summary_final(content, heading, keywords)

    return summary


def get_weighted_words(content):
    doc = tf_idf_base_weighting(content)
    return doc


def get_keywords(content):
    doc = get_document_keywords(content)
    return doc
