class GameState:
    """
    用于管理游戏过程中的状态信息，包括回合、奖池、公共牌等。
    """
    def __init__(self, players):
        self.players = players  # 玩家列表（包括 AI 和人类玩家）
        self.round = 1          # 当前回合数
        self.pot = 0            # 奖池筹码总数
        self.community_cards = []  # 公共牌

    def reset(self):
        """
        重置游戏状态，用于新一轮游戏。
        """
        self.round += 1
        self.pot = 0
        self.community_cards = []
        for player in self.players:
            player.reset()

    def add_to_pot(self, amount):
        """
        增加奖池筹码数。
        """
        self.pot += amount

    def add_community_card(self, card):
        """
        向公共牌中添加一张牌。
        """
        self.community_cards.append(card)

    def display_state(self):
        """
        显示当前游戏状态，包括公共牌和奖池。
        """
        print(f"\n===== 游戏状态 =====")
        print(f"当前回合: {self.round}")
        print(f"奖池总数: {self.pot}")
        print(f"公共牌: {', '.join(self.community_cards) if self.community_cards else '无'}")
        print("====================\n")
