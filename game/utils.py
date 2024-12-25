def display_community_cards(community_cards):
    """显示公共牌"""
    print(f"公共牌: {', '.join(community_cards)}")


def display_player_hand(player):
    """显示玩家的手牌"""
    print(f"{player.name} 的手牌: {', '.join(player.hand)}")
