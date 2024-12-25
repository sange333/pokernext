def display_cards(cards, label="牌"):
    """
    显示一组牌
    """
    if not cards:
        print(f"{label}: 无牌")
    else:
        print(f"{label}: {', '.join(cards)}")


def format_player_status(player):
    """
    格式化玩家状态字符串
    """
    status = f"{player.name} - 筹码: {player.chips}"
    if player.folded:
        status += " (已弃牌)"
    else:
        status += f" (当前下注: {player.bet})"
    return status


def display_player_hands(players):
    """
    显示所有玩家的手牌
    """
    print("\n玩家手牌：")
    for player in players:
        if player.folded:
            print(f"{player.name}: 已弃牌")
        else:
            print(f"{player.name}: {', '.join(player.hand)}")


def display_game_summary(players, community_cards, pot):
    """
    显示当前游戏总结，包括公共牌、玩家筹码和总奖池
    """
    print("\n=== 当前游戏状态 ===")
    display_cards(community_cards, label="公共牌")
    print(f"总奖池: {pot} 筹码")
    print("\n玩家情况：")
    for player in players:
        print(format_player_status(player))
    print("===================")
