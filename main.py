from poker_game import PokerGame

def main():
    print("欢迎来到德州扑克游戏！")
    game = PokerGame()
    for round in range(10):  # 假设最多玩10轮
        print(f"--- 第 {round + 1} 轮 ---")
        game.play_round()

if __name__ == "__main__":
    main()
