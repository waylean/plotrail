<p align="center">
  <img src="assets/plotrail-wordmark.svg" alt="PlotRail wordmark" width="820">
</p>

<p align="center">
  <a href="README.md">中文</a> · <a href="README.en.md">English</a>
</p>

<p align="center">
  <a href="#30-秒安装">安装</a> ·
  <a href="#观看演示">演示视频</a> ·
  <a href="#为什么又做-plotrail-intake">Intake</a> ·
  <a href="#第一条-prompt">第一条 prompt</a> ·
  <a href="#示例假如我成为了反派">真实案例</a>
</p>

# PlotRail 剧情轨

PlotRail 是一个给 Codex、Claude Code 等文件型 AI Agent 使用的长篇小说工作流。它的目标不是让 AI 在一个聊天窗口里硬写完整本书，而是把小说变成一个能长期维护的项目。

现在它包含两个互补的 Skill：

- `novel-writer`：从脑洞、设定、章节合同开始，帮助你把长篇写下去。
- `plotrail-intake`：把已经写好的正文、旧稿、单章片段接进来，诊断、精修、学习风格，并准备交给 PlotRail 继续写。

```text
不要把整本书压进一个 prompt。
PlotRail 给 AI 铺轨：先 canon，再合同，写完必审，旧稿也能入轨。
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

## 为什么做这个项目

AI 已经很会写一段像小说的文字，但长篇真正容易坏在：

- 主线越写越偏
- 人物前后割裂
- 伏笔和秘密被忘掉
- 章节只有事件，没有钩子
- 主角因为剧情需要而赢
- 作者改稿习惯每次都要重新教

我做 PlotRail，是因为我不希望 AI 写长篇时只靠一次聊天里的短期记忆。真正的长篇写作需要设定、人物状态、秘密知情范围、章节目标、伏笔回收、作者偏好都能被持续检查。

作者仍然是导演、第一读者和最终审稿人。PlotRail 更像一个不会偷懒的写作助理：它负责扩展脉络、生成章节合同、写初稿、做连续性审稿、维护状态账本，并从作者修改中学习偏好。

## 为什么又做 plotrail-intake

独立仓库地址：[waylean/plotrail-intake](https://github.com/waylean/plotrail-intake)

我把 PlotRail 发布到抖音、小红书和 B 站后，看到了一些点赞和收藏，但评论很少。其实我最希望看到的，是大家真正使用之后的想法：哪里好用，哪里别扭，哪里还不够像一个能一起写长篇的工具。

也有一些志同道合的小伙伴在做类似方向的工作，让我学到了很多。后来有一位 B 站网友提到：能不能把已经写好的正文一章章喂给 AI，让它不要急着续写，而是更专注地深究正文里的细节。

我觉得这是一个很好的方向。

因为 `novel-writer` 更适合在写作初期建立规范：先 canon、再章节合同、写完后审稿，尽量让故事从一开始就不跑偏。但现实里很多作者并不是从零开始，他们可能已经有一章、几章，甚至一大段自己亲手写过的正文。

这时就需要 `plotrail-intake`：

- 它能单独处理一章临时粘贴的正文。
- 它能诊断已有稿件的问题，而不是默认继续写。
- 它能逐章精修、去 AI 味、学习作者文风。
- 它能做长篇一致性审稿，找出人物、设定、时间线和伏笔风险。
- 它能把已有正文压缩成精简的 `continuation_brief`，交给 `novel-writer` 继续写，避免两个 Skill 重复读取大量无用信息。

我希望这两个 Skill 形成 1+1 大于 2 的效果：`novel-writer` 负责在写作初期建立护栏，`plotrail-intake` 负责在写完之后持续校验和打磨，让文章不偏离、不松散，也不要被润色成统一的 AI 味。

如果你正在写小说，或者已经有一批旧稿，欢迎试试这套组合。也希望你能分享使用体验，哪怕只是告诉我某一章哪里被改得更好了，或者哪里被改坏了。

## 当前版本能做什么

- 从脑洞生成 story proposal，但不会未经批准写入 canon。
- 建立故事圣经、人物关系、时间线和章节合同。
- 在每章开写前明确必须发生、禁止发生、章末钩子和连续性风险。
- 写完后做连续性审稿，检查设定、人设、秘密知情范围和主角行动逻辑。
- 从作者改稿中沉淀编辑画像，让后续章节更接近你的偏好。
- 对已有正文做诊断、逐章精修、风格学习和长篇一致性审稿。
- 在两个 Skill 同时使用时，只传递必要 brief，减少重复上下文。

对应的文件产物：

| 能力 | 文件产物 |
| --- | --- |
| 故事圣经 | `canon/world.md`、`characters.yaml`、`relationships.yaml`、`timeline.yaml` |
| 章节规划 | `outline/chapters.yaml`，每章先有合同再写正文 |
| 正文草稿 | `drafts/chNNN.md`，在 canon 内自由创作 |
| 连续性审稿 | `reviews/chNNN_continuity.md` |
| 长期记忆 | `memory/chapter_summaries.yaml`、`state_ledger.yaml`、`change_requests.yaml` |
| 作者偏好 | `memory/author_editing_profile.md` |
| 已有稿件入轨 | `reviews/`、候选状态账本、风格画像、`outline/continuation_brief_chNNN.md` |

## 两个 Skill 怎么分工

- `novel-writer`：用于从脑洞/设定出发，建立 canon、章节合同、正文草稿、连续性审稿和长期记忆。
- `plotrail-intake`：用于已有正文，包括用户临时粘贴的一章、别人手写的一大段、旧稿文件夹、逐章精修、风格学习、长篇一致性审稿，以及交接给 `novel-writer` 继续写。独立仓库地址：[waylean/plotrail-intake](https://github.com/waylean/plotrail-intake)。

两个 Skill 同时使用时，不要互相复制大量上下文。`plotrail-intake` 先产出精简的 `continuation_brief`，`novel-writer` 再只读取这个 brief 和必要的 canon/memory 文件。

```mermaid
flowchart LR
  A["从零开始"] --> B["novel-writer"]
  B --> C["canon / 章节合同 / 草稿"]
  C --> D["连续性审稿"]
  E["已有正文 / 旧稿 / 单章片段"] --> F["plotrail-intake"]
  F --> G["诊断 / 精修 / 风格学习"]
  G --> H["continuation_brief"]
  H --> B
```

## 30 秒安装

建议同时安装两个互补 Skill：

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.codex/skills
cp -R plotrail/novel-writer ~/.codex/skills/novel-writer
cp -R plotrail/plotrail-intake ~/.codex/skills/plotrail-intake
```

如果 Codex 没有识别，重启 Codex。

Claude Code 可以复制到：

```text
~/.claude/skills/novel-writer
~/.claude/skills/plotrail-intake
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

如果你已经有正文，第一条 prompt 可以改成：

```text
使用 $plotrail-intake。
这是已有小说稿件，请先不要续写。
先诊断稿件状态、找出最值得修的问题，并准备最小可用的下一步。
```

如果你只是想校正一章，可以更直接：

```text
使用 $plotrail-intake。
下面是我已经写好的第 6 章。
请按 light refinement 处理：不要改剧情，不要新增设定。
重点检查节奏、人物动机、去 AI 味、章末钩子和连续性风险。
修改后请列出哪些地方需要作者确认。
```

## 从零开始的工作流

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
如果处理已有稿件，打开 `plotrail-intake/SKILL.md`，并且只加载当前任务需要的 reference，避免把两个 Skill 的全部说明都塞进上下文。

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
plotrail-intake/
  SKILL.md
  references/
    intake-protocol.md
    anti-ai-prose.md
    diagnosis-rubric.md
    refinement-workflow.md
    style-learning.md
    continuity-audit.md
    novel-writer-handoff.md
    shared-context.md
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
