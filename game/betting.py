def collect_bets(players):
    """
    收集玩家的下注金额，计算总奖池。
    如果玩家弃牌（folded），不参与下注。
    """
    total_bet = 0
    for player in players:
        if not player.folded:
            # 检查当前玩家是否需要下注
            total_bet += player.bet
            print(f"{player.name} 下注了 {player.bet} 筹码。")
    return total_bet


def reset_bets(players):
    """
    重置所有玩家的下注金额，用于下一轮游戏。
    """
    for player in players:
        player.bet = 0


def handle_betting_round(players, pot):
    """
    处理一轮下注逻辑：
    玩家和 AI 依次选择下注、加注或弃牌。
    """
    print("\n开始下注轮...")
    current_high_bet = 0  # 当前轮次最高下注金额

    for player in players:
        if player.folded:
            # 如果玩家已经弃牌，跳过
            continue

        if player.is_ai:
            # 如果是 AI 玩家，调用 AI 的决策逻辑
            action = player.make_decision(pot, current_high_bet)
            if action == "call":
                player.bet_chips(current_high_bet - player.bet)
                print(f"{player.name} 跟注了 {current_high_bet} 筹码。")
            elif action == "raise":
                raise_amount = current_high_bet + 10  # 示例加注金额
                player.bet_chips(raise_amount - player.bet)
                current_high_bet = raise_amount
                print(f"{player.name} 加注到 {raise_amount} 筹码。")
            elif action == "fold":
                player.fold()
                print(f"{player.name} 弃牌。")
        else:
            # 如果是人类玩家，提示进行操作
            print(f"\n{player.name} 的筹码: {player.chips}")
            print(f"当前最高下注: {current_high_bet}")
            action = input(f"请选择操作: [1] 跟注 {current_high_bet} [2] 加注 [3] 弃牌: ")
            if action == "1":
                player.bet_chips(current_high_bet - player.bet)
                print(f"{player.name} 跟注了 {current_high_bet} 筹码。")
            elif action == "2":
                raise_amount = int(input("请输入加注金额: "))
                player.bet_chips(raise_amount - player.bet)
                current_high_bet = raise_amount
                print(f"{player.name} 加注到 {raise_amount} 筹码。")
            elif action == "3":
                player.fold()
                print(f"{player.name} 弃牌。")

    # 计算总奖池
    return collect_bets(players)
