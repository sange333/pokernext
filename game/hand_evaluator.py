from collections import Counter

def evaluate_hand(hand):
    # 简单的手牌评估：只返回一个手牌分值
    ranks = [card.split()[0] for card in hand]
    rank_count = Counter(ranks)
    score = sum([rank_count[rank] for rank in rank_count])
    return score

def compare_hands(hand1, hand2):
    score1 = evaluate_hand(hand1)
    score2 = evaluate_hand(hand2)
    if score1 > score2:
        return 1
    elif score2 > score1:
        return -1
    return 0
