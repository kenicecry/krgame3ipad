import random

word_data = [
    ("사과", ["りんご", "パン", "ミルク"], 0),
    ("빵", ["みかん", "パン", "ジュース"], 1),
    ("우유", ["チーズ", "ミルク", "水"], 1)
]

question, options, correct_index = random.choice(word_data)

def check_answer(index):
    return index == correct_index

