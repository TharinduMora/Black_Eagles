import json
from summarization import create_summary
# Make it work for Python 2+3 and with Unicode
import io

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

with open("./Input files/Sample.json", "r") as read_file:
    doc = json.load(read_file)

for data in doc:
    content_summary = create_summary(data['heading'], data['content'])
    data['content'] = content_summary


with io.open('./Output files/summarized_document.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(doc,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
