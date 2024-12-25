from game.poker_game import PokerGame

def main():
    game = PokerGame()
    for i in range(1, 6):  # 假设进行 5 局游戏
        print(f"\n===== 第 {i} 局 =====")
        game.play_game()


if __name__ == "__main__":
    main()
