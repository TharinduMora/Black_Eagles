import io
import json

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def update_prob(word_list, article_id):
    with open("./Input_files/words_with_prob.json", "r") as read_file:
        doc = json.load(read_file)
        prev_number_of_articles = len(doc["article_ids"])

        if prev_number_of_articles == 0:

            for word in word_list:
                doc["words_with_probabilities"].append(
                    {"probability": 1.0 / (prev_number_of_articles + 1), "word": word})

            doc["article_ids"].append(article_id)

        else:

            for obj in doc["words_with_probabilities"]:
                if obj["word"] in word_list:
                    obj["probability"] = (obj["probability"] * prev_number_of_articles + 1.0) / (
                            prev_number_of_articles + 1)
                    word_list.remove(obj["word"])

                else:
                    obj["probability"] = (obj["probability"] * prev_number_of_articles) / (prev_number_of_articles + 1)

            for word in word_list:
                doc["words_with_probabilities"].append(
                    {"probability": 1.0 / (prev_number_of_articles + 1), "word": word})

            doc["article_ids"].append(article_id)

    with io.open('./Input_files/words_with_prob.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(doc,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
