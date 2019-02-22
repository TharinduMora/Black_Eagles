import pymongo
import json

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = my_client["news_db"]

my_col = my_db["word_probability"]

my_col_news = my_db["word_probability"]

my_news = my_db["news"]


# return whole collection
def get_word_probability():
    return my_col


def close_connection():
    my_client.close()


def get_word_probability_list():
    return my_col.find()[0]["words_with_probabilities"]


def get_categorized_news():
    return my_col_news


def get_news_collection():
    return my_news

# def insert_news_to_db():
#     with open("../cricket_news/new2.json", "r") as read_file:
#         doc = json.load(read_file)
#
#     for data in doc:
#         my_news.insert(data)

# insert_news_to_db()
