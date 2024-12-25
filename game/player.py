class Player:
    def __init__(self, name, chips=1000):
        self.name = name          # 玩家名字
        self.chips = chips        # 玩家持有的筹码
        self.hand = []            # 玩家手牌
        self.bet = 0              # 玩家当前下注
        self.folded = False       # 玩家是否弃牌

    def bet_chips(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            self.bet += amount
            return True
        else:
            print(f"{self.name} 筹码不足！")
            return False

    def fold(self):
        self.folded = True
        print(f"{self.name} 放弃了这一轮。")
    
    def reset(self):
        self.hand = []
        self.bet = 0
        self.folded = False
