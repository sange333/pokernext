import random

class AIPlayer(Player):
    def __init__(self, name, chips=1000):
        super().__init__(name, chips)

    def make_decision(self, pot):
        # AI 决策：随机下注、加注或弃牌
        action = random.choice(['bet', 'fold', 'call'])
        if action == 'bet':
            amount = random.randint(10, self.chips)
            self.bet_chips(amount)
        elif action == 'call':
            self.bet_chips(pot)
        else:
            self.fold()
