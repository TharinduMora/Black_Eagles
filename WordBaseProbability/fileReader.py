from word_filter import get_filtered_word_list
from DB_Configurations.db_connection import get_word_probability, get_news_collection
from Probability_Creater_With_DB import update_prob_in_db

# from probability_creater import update_prob
import json

my_col = get_word_probability()
news_col = get_news_collection()

# with open("./Input_files/words_with_prob.json", "r") as read_file:
#     words_doc = json.load(read_file)

words_doc = my_col.find()[0]

doc = news_col.find()
# print doc

# for data in doc:
#     print data["sid"]

# with open("../cricket_news/new2.json", "r") as read_file:
#     # with open("./Input_files/sports_news.json", "r") as read_file:
#     doc = json.load(read_file)
#     number_of_articles = len(doc)

for data in doc:
    if data["sid"] not in words_doc["article_ids"]:
        original_word_list = get_filtered_word_list(data['content'])
        update_prob_in_db(original_word_list, data['sid'])
