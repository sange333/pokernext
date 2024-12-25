def check_winner(players, community_cards):
    """检查谁赢得了本轮游戏"""
    best_score = -1
    winner = None

    for player in players:
        if not player.folded:
            hand = player.hand + community_cards
            score = evaluate_hand(hand)
            print(f"{player.name} 的最终手牌: {hand}, 分值: {score}")
            if score > best_score:
                best_score = score
                winner = player

    return winner
