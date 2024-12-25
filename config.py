# 配置文件，存储游戏相关的常量和规则

# 扑克的花色和点数
SUITS = ['红桃', '黑桃', '梅花', '方块']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# 游戏初始设置
STARTING_CHIPS = 1000  # 每位玩家的初始筹码数
PLAYER_COUNT = 1       # 人类玩家数量
AI_COUNT = 5           # AI 玩家数量

# 游戏逻辑
MAX_ROUNDS = 10        # 最大游戏局数
BET_MINIMUM = 10       # 最小下注金额

# 显示设置
SHOW_PLAYER_HANDS = True  # 是否显示所有玩家手牌（用于调试）
