import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = my_client["news_db"]

my_col = my_db["word_probability"]

my_col_news = my_db["word_probability"]


# return whole collection
def get_word_probability():
    return my_col


def close_connection():
    my_client.close()


def get_word_probability_list():
    return my_col.find()[0]["words_with_probabilities"]


def get_categorized_news():
    return my_col_news