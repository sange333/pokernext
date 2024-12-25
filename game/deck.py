import random
from config import SUITS, RANKS

class Deck:
    def __init__(self):
        # 初始化扑克牌组
        self.cards = [f'{rank} {suit}' for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)  # 洗牌

    def draw_card(self):
        # 发牌
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def reset_deck(self):
        # 重置牌组
        self.cards = [f'{rank} {suit}' for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)
