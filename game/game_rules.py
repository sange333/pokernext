from game.hand_evaluator import evaluate_hand


def check_winner(players, community_cards):
    """
    根据玩家的手牌和公共牌，判断本轮的赢家。
    玩家手牌 + 公共牌 组成完整的牌组用于比较。
    返回获胜玩家。
    """
    best_score = -1
    winner = None

    print("\n开始比较玩家手牌...")
    for player in players:
        if not player.folded:
            # 合并玩家手牌和公共牌
            full_hand = player.hand + community_cards
            score = evaluate_hand(full_hand)

            print(f"{player.name} 的手牌: {player.hand}")
            print(f"公共牌: {community_cards}")
            print(f"{player.name} 的完整手牌分值: {score}\n")

            # 更新最高分玩家
            if score > best_score:
                best_score = score
                winner = player

    if winner:
        print(f"赢家是: {winner.name}，得分: {best_score}")
    else:
        print("没有玩家获胜！")

    return winner
