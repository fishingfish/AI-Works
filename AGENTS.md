# AGENTS.md

本仓库的完整操作说明（同步上游流程、个性化清单、开源合规要求、提交约定）都在 [`CLAUDE.md`](./CLAUDE.md)。
无论你是哪种 AI 编程助手，开始工作前请先完整阅读并遵循 `CLAUDE.md`。

要点速览：

- 用户说“同步上游”时，按 `CLAUDE.md` 的流程：拉取上游、汇报改动、保留个性化、跑 `python3 scripts/check.py`，经用户确认再推送到 `main`。
- 修改配置后必须运行 `python3 scripts/check.py`，输出 `OK` 才算完成。
- 不要提交节点、订阅链接、密码或服务商模块；不要删除 `LICENSE` 里原作者的版权行。
