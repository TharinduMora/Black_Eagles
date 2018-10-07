# -*- coding: utf-8 -*-
from keywordExtraction import get_keywords
from sentencesAnalyzing import get_content_summary

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def create_summary(heading, content):
    content = content.replace('COLOMBO (News 1st) : ', '')
    content = content.replace('COLOMBO (News 1st) – ', '')

    keywords = get_keywords(content, heading)
    summary = get_content_summary(content, keywords)

    return summary
