def collect_bets(players):
    total_bet = 0
    for player in players:
        if not player.folded:
            bet = player.bet
            total_bet += bet
            print(f"{player.name} 下注了 {bet} 筹码。")
    return total_bet

def reset_bets(players):
    for player in players:
        player.bet = 0
