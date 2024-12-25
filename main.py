from game.poker_game import PokerGame
from config import MAX_ROUNDS, STARTING_CHIPS, PLAYER_COUNT, AI_COUNT  # 导入配置常量


def main():
    """
    游戏主入口，启动德州扑克游戏。
    """
    print("欢迎来到德州扑克游戏！\n")
    print("游戏规则：")
    print(f"- 每位玩家初始拥有 {STARTING_CHIPS} 筹码")
    print(f"- 游戏最多进行 {MAX_ROUNDS} 局")
    print(f"- 人类玩家: {PLAYER_COUNT} 名，AI 玩家: {AI_COUNT} 名")
    print("- 每轮包括发手牌、公共牌、下注和决胜阶段\n")
    
    # 初始化游戏
    game = PokerGame()
    
    # 连续进行多局游戏
    game.play_multiple_games(num_games=MAX_ROUNDS)

    print("\n感谢游玩德州扑克游戏！")


if __name__ == "__main__":
    main()
