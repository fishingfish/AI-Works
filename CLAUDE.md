# 仓库说明（给 AI 助手）

这是 fishingfish 个人维护的 Shadowrocket 配置，基于 LingJingMaster/Shadowrocket-Rules（MIT）修改而来。
订阅地址：`https://raw.githubusercontent.com/fishingfish/AI-Works/refs/heads/main/Shadowrocket_fish.conf`

## 同步上游（用户说“同步上游”时执行）

1. `git remote add upstream https://github.com/LingJingMaster/Shadowrocket-Rules.git`（已存在则跳过），`git fetch upstream main`。
2. 在 `main` 的基础上新建分支，`git merge upstream/main`；先用 `git log HEAD..upstream/main --oneline` 向用户汇报上游改了什么。
3. 解决冲突时**保留用户的个性化**（见下），只吸收有价值的上游改动。不要自动采用上游整份文件。
4. 运行 `python3 scripts/check.py`，必须输出 OK。
5. 把合并结果和“吸收了什么、没吸收什么”告诉用户，用户确认后再推送到 `main`。

## 个性化清单（合并时必须保留）

- 配置文件改名为 `Shadowrocket_fish.conf`；上游的 `Shadowrocket.conf` 改动需手动移植到它。`update-url` 与所有自有 `.list` 链接指向 `fishingfish/AI-Works`，不要改回上游。
- 去广告：`AdvertisingLite`（RULE-SET + DOMAIN-SET），策略组 `🛑 广告拦截`；不使用 MITM 与 URL Rewrite。
- 策略组：新增 `🧩 自定义规则`、`🎬 流媒体`、`💬 社交平台`、`🇸🇬 新加坡节点`、`🎮 游戏节点`；Telegram 并入 `💬 社交平台`、YouTube（含翻译 API）并入 `🎬 流媒体`（不再有电报/油管单独策略组）；已删除台湾节点、汇丰、香港银行、券商相关组。
- 节点筛选：地区组为手动 `select`，过滤名称含 家宽/星链/住宅/5X/游戏 的节点；美国组同样过滤这些。`🤖 AI 服务` 只包含名称含“家宽”或“星链”的美国节点（排除“游戏”），没有其他备选，默认选中节点名“🇺🇸 美国-家宽 02丨5x US”（`policy-select-name`）。`🚀 节点选择` 默认新加坡节点。
- 谷歌服务默认美国节点。国内 DoH：`[Host]` 中国内域名使用阿里 DoH。
- 已删除的文件不要恢复：`HSBC_HK.list`、`HK_Banks_Direct.list`、`HK_Broker.list`。上游若更新它们，选择继续删除。
- `Netflix.list`、`Facebook.list`、`Custom.list`、`qrcode.png` 为本仓库自有文件，上游没有。
- `Google.list`、`AI.list` 已删除被广告规则覆盖的条目、`AI.list` 补充了若干 AI 服务；上游新增域名可吸收，但不要加回已被广告规则覆盖的广告域名。

## 开源合规

- `LICENSE` 必须保留原作者版权行（Ling_Jing）及 MIT 文本；README 的“规则集来源”保留对 LingJingMaster、blackmatrix7、iab0x00 的署名。
- blackmatrix7/ios_rule_script 为 GPL-2.0：只在线引用其规则文件，不要把它的规则大段复制进本仓库。
- 仓库公开：不得提交节点、订阅链接、密码或服务商的模块内容。

## 提交约定

每次修改后更新 README 末尾的“我的修改记录”。
