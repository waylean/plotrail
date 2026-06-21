# 安装 PlotRail

PlotRail 的公开仓库名是 `plotrail`。它现在包含两个可以安装的互补 Skill：

- `novel-writer`：从已批准的 canon 和章节合同出发，规划、起草、审稿并维护长篇小说。
- `plotrail-intake`：诊断已有正文、摄取旧稿、精修草稿、学习作者风格、审查连续性，并为 `novel-writer` 准备精简交接。

## Codex：macOS 或 Linux

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.codex/skills
cp -R plotrail/novel-writer ~/.codex/skills/novel-writer
cp -R plotrail/plotrail-intake ~/.codex/skills/plotrail-intake
```

如果 Skill 没有出现，重启 Codex。

## Claude Code：macOS 或 Linux

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.claude/skills
cp -R plotrail/novel-writer ~/.claude/skills/novel-writer
cp -R plotrail/plotrail-intake ~/.claude/skills/plotrail-intake
```

如有需要，重启 Claude Code。

## Codex：Windows PowerShell

```powershell
git clone https://github.com/waylean/plotrail.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\plotrail\novel-writer" "$env:USERPROFILE\.codex\skills\novel-writer"
Copy-Item -Recurse -Force ".\plotrail\plotrail-intake" "$env:USERPROFILE\.codex\skills\plotrail-intake"
```

## 快速测试

创建一个空项目：

```bash
python3 ~/.codex/skills/novel-writer/scripts/init_novel_project.py /tmp/plotrail-demo
```

然后在你的 Agent 中打开 `/tmp/plotrail-demo`，运行 README 里的第一条 prompt。

测试 `plotrail-intake` 时，可以粘贴一章已有正文并输入：

```text
使用 $plotrail-intake。
先诊断这一章。暂时不要重写。
```

## 手动模式

如果你的 Agent 不支持自动加载 Skill：

1. 需要规划和写新章节时，打开 `novel-writer/SKILL.md`。
2. 需要诊断、摄取、精修和交接已有稿件时，打开 `plotrail-intake/SKILL.md`。
3. 只加载当前任务需要的 `references/` 文件，避免把所有说明都塞进上下文。
4. 从零开始长篇项目时，可用 `novel-writer/scripts/init_novel_project.py` 创建稳定的项目目录。
