from collections import Counter


def evaluate_hand(hand):
    """评估手牌强度"""
    ranks = [card.split()[0] for card in hand]
    suits = [card.split()[1] for card in hand]

    # 统计点数和花色
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    # 判断是否为同花
    is_flush = max(suit_counts.values()) >= 5

    # 判断点数顺子
    rank_order = '23456789TJQKA'
    rank_indexes = sorted([rank_order.index(rank) for rank in ranks])
    is_straight = len(rank_indexes) >= 5 and all(
        rank_indexes[i] + 1 == rank_indexes[i + 1] for i in range(len(rank_indexes) - 1)
    )

    # 根据组合类型返回分值（可扩展）
    if is_flush and is_straight:
        return 100  # 同花顺
    elif max(rank_counts.values()) == 4:
        return 80  # 四条
    elif sorted(rank_counts.values()) == [2, 3]:
        return 60  # 葫芦
    elif is_flush:
        return 40  # 同花
    elif is_straight:
        return 20  # 顺子
    elif max(rank_counts.values()) == 3:
        return 15  # 三条
    elif sorted(rank_counts.values()) == [1, 2, 2]:
        return 10  # 两对
    elif 2 in rank_counts.values():
        return 5  # 一对
    else:
        return max(rank_indexes)  # 高牌


def compare_hands(hand1, hand2):
    """比较两副手牌，返回胜负"""
    score1 = evaluate_hand(hand1)
    score2 = evaluate_hand(hand2)
    if score1 > score2:
        return 1
    elif score2 > score1:
        return -1
    else:
        return 0
