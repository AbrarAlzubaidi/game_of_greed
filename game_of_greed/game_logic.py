from collections import Counter

class GameLogic:

    @staticmethod
    def calculate_score(item):
        item = Counter(item)
        score = 0
        if len(item) == 6:
            for i in item.values():
                if i == 1:
                    score = 1500
        if len(item) == 3:
            for i in item.values():
                if all(i == 2 for i in item.values()):
                    score = 750 * 2
        if score == 0:
            for i in item:
                happened = item[i]
                if happened >= 3:
                    if i == 1:
                        score += (i * 1000) * (happened-2)
                    else:
                        score += (i * 100) * (happened-2)
                else:
                    if i == 1:
                        score += 100*happened
                    if i == 5:
                        score += 50*happened
        return score
