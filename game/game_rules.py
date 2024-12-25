def check_winner(players, community_cards):
    # 比较每个玩家的手牌与公共牌，评估谁的牌更大
    best_hand = None
    winner = None
    for player in players:
        if not player.folded:
            hand = player.hand + community_cards
            score = evaluate_hand(hand)
            if best_hand is None or score > best_hand:
                best_hand = score
                winner = player
    return winner
