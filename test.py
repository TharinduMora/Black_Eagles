import json
from summarization import create_summary, get_weighted_words, get_keywords
# Make it work for Python 2+3 and with Unicode
import io

from DB_Configurations.db_connection import get_categorized_news

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# with open("./Input files/Sample.json", "r") as read_file:
#     doc = json.load(read_file)
#
# for data in doc:
#     content_summary = create_summary(data['heading'], data['content'])
#     data['content'] = content_summary
#
# with io.open('./Output files/summarized_document.json', 'w', encoding='utf8') as outfile:
#     str_ = json.dumps(doc,
#                       indent=4, sort_keys=True,
#                       separators=(',', ': '), ensure_ascii=False)
#     outfile.write(to_unicode(str_))


with open("./cricket_news/new.json", "r") as read_file:
    doc = json.load(read_file)
    cric_news = []

    # my_collection = get_categorized_news()

    for data in doc:

        if int(data['sid']) < 501:
            cric_news.append(data)

        # my_collection.insert(data)

    # my_collection.insert(doc)

with io.open('./Output files/new2.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(cric_news,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
