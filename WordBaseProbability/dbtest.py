from DB_Configurations.db_connection import get_word_probability
from DB_Configurations.db_connection import close_connection

my_col = get_word_probability()


def remove():
    my_col.update({}, {
        "article_ids": [],
        "words_with_probabilities": []
    })
    # close_connection()


def show():
    doc = my_col.find()[0]

    for x in doc["words_with_probabilities"]:
        if x['probability'] > 0.3:
            print x['probability'], x['word']

    # close_connection()


# remove()
show()
