import random
from game.player import Player


class AIPlayer(Player):
    def __init__(self, name, chips=1000):
        """初始化 AI 玩家，继承自 Player 类"""
        super().__init__(name, chips)

    def make_decision(self, pot, community_cards):
        """
        AI 玩家决策逻辑：
        - AI 基于随机选择进行决策
        - 可以进一步扩展为基于手牌和公共牌的概率计算
        """
        print(f"{self.name} 正在思考...")
        action = random.choice(["call", "raise", "fold"])  # 随机选择动作
        if action == "call":
            # 跟注
            bet_amount = min(self.chips, pot)
            self.bet_chips(bet_amount)
            print(f"{self.name} 选择跟注，下注了 {bet_amount} 筹码。")
        elif action == "raise":
            # 加注
            raise_amount = random.randint(10, min(self.chips, pot + 50))
            self.bet_chips(raise_amount)
            print(f"{self.name} 选择加注，下注了 {raise_amount} 筹码。")
        elif action == "fold":
            # 弃牌
            self.fold()
