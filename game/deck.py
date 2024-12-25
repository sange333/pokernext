import random
from config import SUITS, RANKS


class Deck:
    def __init__(self):
        """
        初始化扑克牌组，包括52张牌。
        每张牌由点数和花色组成，例如 "A 红桃"。
        """
        self.cards = [f"{rank} {suit}" for suit in SUITS for rank in RANKS]
        self.shuffle_deck()

    def shuffle_deck(self):
        """
        洗牌，将牌组随机打乱。
        """
        random.shuffle(self.cards)
        print("牌组已洗牌！")

    def draw_card(self):
        """
        从牌组顶部抽取一张牌。
        如果牌组为空，返回 None。
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("牌组已空，无法继续发牌。")
            return None

    def reset_deck(self):
        """
        重置牌组到初始状态并洗牌。
        """
        self.cards = [f"{rank} {suit}" for suit in SUITS for rank in RANKS]
        self.shuffle_deck()
