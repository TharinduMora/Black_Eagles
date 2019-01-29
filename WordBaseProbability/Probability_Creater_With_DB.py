from DB_Configurations.db_connection import get_word_probability

my_col = get_word_probability()


def update_prob_in_db(word_list, article_id):
    doc = my_col.find()[0]
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

    doc["words_with_probabilities"].sort(reverse=True, key=sort_by_probability)

    my_col.remove()
    my_col.insert(doc)


def sort_by_probability(e):
    return e['probability']
