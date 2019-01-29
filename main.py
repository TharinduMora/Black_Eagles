import json
from summarization import create_summary, get_weighted_words, get_keywords
# Make it work for Python 2+3 and with Unicode
import io

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


with open("./cricket_news/sports_news.json", "r") as read_file:
    doc = json.load(read_file)

for data in doc:
    # weighted_doc = get_weighted_words(data['content'])
    # data['tf_idf_weight_list'] = weighted_doc
    # keywords = get_keywords(data['content'])
    # data['keywords'] = keywords
    data['summary'] = create_summary(None , data['content'])
    # break

with io.open('./Output files/summarized_document.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(doc,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
