class Player:
    """
    玩家类，表示游戏中的一个玩家（人类或 AI）。
    """
    def __init__(self, name, chips=1000, is_ai=False):
        self.name = name          # 玩家名字
        self.chips = chips        # 玩家拥有的筹码
        self.hand = []            # 玩家手牌
        self.bet = 0              # 当前下注金额
        self.folded = False       # 玩家是否已弃牌
        self.is_ai = is_ai        # 是否为 AI 玩家

    def bet_chips(self, amount):
        """
        玩家下注一定金额的筹码。如果筹码不足，则无法下注。
        """
        if amount <= self.chips:
            self.chips -= amount
            self.bet += amount
            return True
        else:
            print(f"{self.name} 筹码不足，无法下注 {amount}！")
            return False

    def fold(self):
        """
        玩家弃牌。
        """
        self.folded = True
        print(f"{self.name} 选择弃牌。")

    def reset(self):
        """
        重置玩家状态，用于下一轮游戏。
        """
        self.hand = []
        self.bet = 0
        self.folded = False
