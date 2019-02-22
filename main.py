import json
from summarization import create_summary, get_weighted_words, get_keywords
from DB_Configurations.db_connection import get_news_collection
# Make it work for Python 2+3 and with Unicode
import io
from bson import json_util

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

news_col = get_news_collection()
doc = news_col.find()
# doc = json.dumps(news_col.find(), default=json_util.default)
# with open("./cricket_news/sports_news.json", "r") as read_file:
#     doc = json.load(read_file)

txt = []
for data in doc:
    del data['_id']
    if not data['content']:
        continue
    txt.append(
        {"category": data['category'],
         "summary": create_summary(data['title'], data['content']),
         "date": data['date'],
         "sid": data['sid'],
         "title": data['title'],
         "wid": data['wid']
         })
    # weighted_doc = get_weighted_words(data['content'])
    # data['tf_idf_weight_list'] = weighted_doc
    # keywords = get_keywords(data['content'])
    # data['keywords'] = keywords
    # data['summary'] = create_summary(None, data['content'])
    # break

with io.open('./Output files/summarized_document.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(txt,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
