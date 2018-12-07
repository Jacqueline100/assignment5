import random

import nltk
from nltk.corpus import senseval
from nltk.corpus.reader.senseval import SensevalInstance
from interest import create_labeled_data
from interest import wsd_features
from interest import create_feature_sets

def analysis():
    interest = senseval.instances('interest.pos')
    labeled_data = create_labeled_data()

    set1 = [data for data in labeled_data if data[1] == 'interest_1']
    set2 = [data for data in labeled_data if data[1] == 'interest_2']
    set3 = [data for data in labeled_data if data[1] == 'interest_3']
    set4 = [data for data in labeled_data if data[1] == 'interest_4']
    set5 = [data for data in labeled_data if data[1] == 'interest_5']
    set6 = [data for data in labeled_data if data[1] == 'interest_6']

    def most_frequent_content_words(set):
        fdist1 = nltk.FreqDist(set)
        return fdist1.most_common(3)

    word_set1 = [d[0]['word'] for d in set1]
    word_set2 = [d[0]['word'] for d in set2]
    word_set3 = [d[0]['word'] for d in set3]
    word_set4 = [d[0]['word'] for d in set4]
    word_set5 = [d[0]['word'] for d in set5]
    word_set6 = [d[0]['word'] for d in set6]

    print("The most 3 frequent word occurs after interest_1 is: ", most_frequent_content_words(word_set1))
    print("The most 3 frequent word occurs after interest_2 is: ", most_frequent_content_words(word_set2))
    print("The most 3 frequent word occurs after interest_3 is: ", most_frequent_content_words(word_set3))
    print("The most 3 frequent word occurs after interest_4 is: ", most_frequent_content_words(word_set4))
    print("The most 3 frequent word occurs after interest_5 is: ", most_frequent_content_words(word_set5))
    print("The most 3 frequent word occurs after interest_6 is: ", most_frequent_content_words(word_set6))
    

    tag_set1 = [d[0]['word_tag'] for d in set1]
    tag_set2 = [d[0]['word_tag'] for d in set2]
    tag_set3 = [d[0]['word_tag'] for d in set3]
    tag_set4 = [d[0]['word_tag'] for d in set4]
    tag_set5 = [d[0]['word_tag'] for d in set5]
    tag_set6 = [d[0]['word_tag'] for d in set6]

    print("The most 3 frequent properties occurs after interest_1 is: ", most_frequent_content_words(tag_set1))
    print("The most 3 frequent properties occurs after interest_2 is: ", most_frequent_content_words(tag_set2))
    print("The most 3 frequent properties occurs after interest_3 is: ", most_frequent_content_words(tag_set3))
    print("The most 3 frequent properties occurs after interest_4 is: ", most_frequent_content_words(tag_set4))
    print("The most 3 frequent properties occurs after interest_5 is: ", most_frequent_content_words(tag_set5))
    print("The most 3 frequent properties occurs after interest_6 is: ", most_frequent_content_words(tag_set6))
    

    previousword1 = [d[0]['previous_word'] for d in set1]
    previousword2 = [d[0]['previous_word'] for d in set2]
    previousword3 = [d[0]['previous_word'] for d in set3]
    previousword4 = [d[0]['previous_word'] for d in set4]
    previousword5 = [d[0]['previous_word'] for d in set5]
    previousword6 = [d[0]['previous_word'] for d in set6]

    print("The most 3 frequent word occurs before interest_1 is: ", most_frequent_content_words(previousword1))
    print("The most 3 frequent word occurs before interest_2 is: ", most_frequent_content_words(previousword2))
    print("The most 3 frequent word occurs before interest_3 is: ", most_frequent_content_words(previousword3))
    print("The most 3 frequent word occurs before interest_4 is: ", most_frequent_content_words(previousword4))
    print("The most 3 frequent word occurs before interest_5 is: ", most_frequent_content_words(previousword5))
    print("The most 3 frequent word occurs before interest_6 is: ", most_frequent_content_words(previousword6))
