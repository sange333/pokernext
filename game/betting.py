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
            elif action == "raise":
                raise_amount = current_high_bet + 10  # 示例加注金额
                player.bet_chips(raise_amount - player.bet)
                current_high_bet = raise_amount
            elif action == "fold":
                player.fold()
        else:
            # 如果是人类玩家，提示进行操作
            print(f"\n{player.name} 的筹码: {player.chips}")
            action = input(f"请选择操作: [1] 跟注 {current_high_bet} [2] 加注 [3] 弃牌: ")
            if action == "1":
                player.bet_chips(current_high_bet - player.bet)
            elif action == "2":
                raise_amount = int(input("请输入加注金额: "))
                player.bet_chips(raise_amount - player.bet)
                current_high_bet = raise_amount
            elif action == "3":
                player.fold()
                print(f"{player.name} 弃牌。")

    # 计算总奖池
    return sum(player.bet for player in players if not player.folded)
