def transform(old):
    return collect(format(extract(old)))


def format(pair_list):
    updated = []
    for pair in pair_list:
        updated.append(pair.get_pair_with_lowercase_word())
    return updated


def extract(old):
    flattened = []
    for score, word_list in old.items():
        flattened.extend(split_into_pairs(score, word_list))
    return flattened


def collect(flattened):
    collected = {}
    for pair in flattened:
        collected[pair.get_word()] = pair.get_score()
    return collected


def split_into_pairs(score, word_list):
    pair_list = []
    for word in word_list:
        pair_list.append(Pair(score, word))
    return pair_list


class Pair:
    def __init__(self, score, word):
        self.score = score
        self.word = word

    def get_word(self):
        return self.word

    def get_score(self):
        return self.score

    def get_pair_with_lowercase_word(self):
        return Pair(self.score, self.word.lower())
