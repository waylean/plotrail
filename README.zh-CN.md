<p align="center">
  <img src="assets/plotrail-wordmark.svg" alt="PlotRail wordmark" width="820">
</p>

<p align="center">
  <a href="README.zh-CN.md">中文</a> · <a href="README.md">English</a>
</p>

<p align="center">
  <a href="#30-秒安装">安装</a> ·
  <a href="#观看演示">演示视频</a> ·
  <a href="#第一条-prompt">第一条 prompt</a> ·
  <a href="#示例假如我成为了反派">真实案例</a>
</p>

# PlotRail 剧情轨

PlotRail 是一个给 Codex、Claude Code 等文件型 AI Agent 使用的长篇小说写作 Skill，用来让 AI 长篇创作不丢主线、不忘人设、不乱伏笔。

它不会让 AI 在一个聊天窗口里硬记整本书，而是把小说变成一个长期项目：设定库、章节合同、正文草稿、连续性审稿、素材池、状态账本、作者编辑画像，全都落在文件里。

```text
不要把整本书压进一个 prompt。
PlotRail 给 AI 铺轨：先 canon，再合同，写完必审，改稿会沉淀。
```

## 观看演示

<p align="center">
  <a href="assets/plotrail-promo.mp4">
    <img src="assets/plotrail-promo-preview.gif" alt="PlotRail 演示视频预览" width="360">
  </a>
</p>

<p align="center">
  <a href="assets/plotrail-promo.mp4"><strong>观看完整 42 秒 MP4 演示视频</strong></a>
</p>

## 为什么值得安装

AI 已经很会写一段像小说的文字，但长篇真正容易坏在：

- 主线越写越偏
- 人物前后割裂
- 伏笔和秘密被忘掉
- 章节只有事件，没有钩子
- 主角因为剧情需要而赢
- 作者改稿习惯每次都要重新教

PlotRail 的目标是让 AI 从“会写一段”变成“能协助长期连载”。作者仍然是导演、第一读者和最终审稿人；AI 负责扩展脉络、生成章节合同、写初稿、做连续性审稿、维护状态账本，并从作者修改中学习偏好。

## 它会创建什么

| 能力 | 文件产物 |
| --- | --- |
| 故事圣经 | `canon/world.md`、`characters.yaml`、`relationships.yaml`、`timeline.yaml` |
| 章节规划 | `outline/chapters.yaml`，每章先有合同再写正文 |
| 正文草稿 | `drafts/chNNN.md`，在 canon 内自由创作 |
| 连续性审稿 | `reviews/chNNN_continuity.md` |
| 长期记忆 | `memory/chapter_summaries.yaml`、`state_ledger.yaml`、`change_requests.yaml` |
| 作者偏好 | `memory/author_editing_profile.md` |

## 30 秒安装

当前可安装的 Skill 文件夹名仍然是 `novel-writer`。

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.codex/skills
cp -R plotrail/novel-writer ~/.codex/skills/novel-writer
```

如果 Codex 没有识别，重启 Codex。

Claude Code 可以复制到：

```text
~/.claude/skills/novel-writer
```

更多安装方式见 [INSTALL.md](INSTALL.md)。

## 第一条 prompt

新建一个小说文件夹，在 Codex 或 Claude Code 里打开它，然后说：

```text
使用 novel-writer skill。

请初始化这个文件夹为长篇小说项目。
先不要写正文。

请先根据我提供的主题、脑洞、目标读者、雷点、
风格参考和结局倾向，生成 3 个 story proposal。
未经我批准，不要写入 canon。
```

然后补充：

```text
主题：
脑洞：
类型：
目标读者：
主角：
反派：
我喜欢的作品：
我不想要的雷点：
结局倾向：
平台/篇幅目标：
```

## 工作流

```mermaid
flowchart LR
  A["脑洞"] --> B["Proposal"]
  B --> C["批准后写入 canon"]
  C --> D["章节合同"]
  D --> E["正文草稿"]
  E --> F["连续性审稿"]
  F --> G["作者修改"]
  G --> H["状态账本和编辑画像"]
  H --> D
```

1. 作者给主题、脑洞、目标读者、雷点、风格参考。
2. AI 先生成 proposal，不直接写入 canon。
3. 作者审批方向。
4. AI 把批准内容写入 `canon/` 和 `outline/`。
5. 每章先生成章节合同。
6. 作者批准章节合同后再写正文。
7. 写完后做连续性审稿，检查 canon、人设、秘密知情范围、时间线和钩子强度。
8. 作者修改后，AI 把偏好沉淀进作者编辑画像。

## 示例：《假如我成为了反派》

[`examples/假如我成为了反派/`](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/) 里放了一个真实项目的结构化案例。

前 11 章展示了这个工作流如何改善：

- 主角主动性：不是因为剧情需要而成功，而是有步骤、约束、备选方案和代价
- 反派组织可信度
- 规则说明时机
- 章末钩子
- 夺舍后的道德代价
- 长篇连载中的连续性

从作者改稿中提炼出的核心偏好：

```text
不要让主角因为剧情需要而赢。
要展示流程、约束、测试、备选方案和代价。
```

可以直接打开这些证明文件：

- [章节合同样例](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/sample-chapter-contract.md)
- [连续性审稿样例](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/sample-continuity-review.md)
- [作者编辑画像](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/author-editing-profile.md)

## 适用于什么模型

PlotRail 不绑定某一个模型。它适合所有能读取本地文件、写文件、遵循 `SKILL.md` 流程的 Agent。

推荐：

- Codex + 强推理/强代码模型
- Claude Code + Skills 支持
- 其他支持 `SKILL.md`、文件读写、长流程执行的 Agent

如果你的工具不支持自动加载 Skill，也可以手动打开 `novel-writer/SKILL.md`，把里面的核心规则复制到系统提示词或项目说明里，再把 `novel-writer/references/` 作为项目知识库使用。

## 仓库结构

```text
novel-writer/
  SKILL.md
  references/
    canon-schemas.md
    chapter-workflow.md
    human-edit-loop.md
  scripts/
    init_novel_project.py
examples/
  假如我成为了反派/
assets/
  plotrail-wordmark.svg
  plotrail-promo-preview.gif
  plotrail-promo.mp4
```

## 更名说明

PlotRail 剧情轨原名 `novel-writer`。因为 `novel-writer` 过于泛化，无法准确表达项目真正解决的问题，所以现在更名为 PlotRail 剧情轨。本版本中，可安装的 Skill 文件夹和调用名仍保留为 `novel-writer`，以兼容已经安装和正在使用的项目。

## 许可证

MIT License。
