德州扑克命令行游戏
项目简介
这是一个基于命令行的德州扑克游戏，包含 1 名玩家与 5 名 AI 玩家，支持完整的德州扑克游戏流程，包括发手牌、下注、发公共牌和决胜环节。通过清晰的代码架构和模块化设计，用户可以轻松地运行游戏并扩展功能。

功能特色
完整的德州扑克游戏流程：
发放手牌和公共牌
玩家和 AI 的下注机制
自动计算胜负逻辑
AI 玩家：
简单的随机决策逻辑（加注、跟注或弃牌）
可扩展为更复杂的策略
玩家互动：
人类玩家可以自由选择操作（跟注、加注或弃牌）
模块化设计：
各功能模块分开设计，便于理解和扩展

游戏规则
每位玩家（包括 AI 和人类玩家）初始拥有 1000 筹码。
游戏流程：
发手牌：每位玩家获得两张手牌。
翻牌前下注：玩家和 AI 选择下注、加注或弃牌。
翻牌：发出三张公共牌，玩家继续下注。
转牌：发出第四张公共牌，玩家继续下注。
河牌：发出第五张公共牌，进行最后一轮下注。
决胜：比较玩家手牌与公共牌的组合，得分最高者胜出并赢得奖池。
游戏最多进行 10 局，或玩家筹码不足时游戏结束。