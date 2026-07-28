# Agent Skills for Enterprise Transformation

[English](README.en.md) · [Agent Skills 标准](https://agentskills.io/)

面向传统企业内部转型的五段式 Flight Cycle Agent Skills：开工前看世界，方案前找边界，决策中做融合，交付后做验收，跨周期做复盘。

这不是一套承诺“包治百病”的转型方法论，也不是五个彼此孤立的提示词。它们是一组轻量工作闸门，帮助人和 AI 在真实约束下少走弯路、保留证据、形成自己的解法，并让一次项目经验进入下一轮。

> 公开版来自真实工作方法，但已移除公司、客户、项目、地点、内部系统、账号、路径、真实问题、日志与其他可识别信息。仓库中的案例均为重新组合的虚构示例。

## 五段闭环

```mermaid
flowchart LR
    A["Preflight<br/>先查前例"] --> B["Scale<br/>找到工作边界"]
    B --> C["Fusion<br/>形成自有解法"]
    C --> D["执行与验证"]
    D --> E["Postflight<br/>验收与长久化"]
    E --> F["Retro Insights<br/>跨周期复盘"]
    F -. "经证据验证的改进" .-> A
```

| Skill | 它回答的问题 | 不替代什么 |
|---|---|---|
| [`preflight`](skills/preflight/) | 别人做过什么？什么值得借，什么不该做？ | 深度研究、方案设计、实施 |
| [`scale`](skills/scale/) | 同一问题要向外、向内和横向看到哪里，才能行动？ | 固定层级划分、详细方案 |
| [`fusion`](skills/fusion/) | 如何吸收多个方向的精华，形成自洽的新解法？ | 复制、拼贴、广泛找前例 |
| [`postflight`](skills/postflight/) | 结果真的完成了吗？能否恢复、维护和交接？ | 开工调研、继续扩项 |
| [`retro-insights`](skills/retro-insights/) | 多次任务后，哪些模式值得进入下一周期？ | 单次验收、自动改写长期规则 |

## 为什么为传统企业内部转型而开源

传统企业的转型很少从一张白纸开始。它通常发生在既有流程、遗留系统、组织边界、合规要求、供应商能力、历史承诺和一线经验共同作用的环境中。

真正困难的不是“有没有一个新工具”，而是：

- 新工具是否解决了真实问题，而不是制造演示效果；
- 局部优化是否把成本转移给了别的团队；
- 外部最佳实践能否穿过本企业的约束；
- 方案是否能从试点走向可验收、可恢复、可维护；
- 一次项目的教训是否能成为下一次更好的起点。

我开源这五个 Skills，希望与传统行业的产品、运营、IT、流程改进、数字化与 AI 实践者交流：分享可复用的判断方式，而不是暴露任何一家企业的内部答案；共同讨论哪些方法能够跨组织迁移，哪些必须留给现场重新判断。

## 哲学支撑

这些 Skills 与几类思想有明确亲缘关系：

- **实用主义**：一个观点的价值要落到行动后果和可验证结果上。
- **系统思维**：问题存在于关系、反馈和约束中，不能只优化孤立节点。
- **可错论**：方案只是当前证据下的最好解释，必须允许反例、纠正和回退。
- **辩证的综合**：融合不是取平均数，而是在矛盾和约束中重组出新的整体。
- **持续改进**：完成不是终点；但改进也不能脱离证据、无限扩张成新项目。

### 我的个人哲学观

> 我不把传统企业看作等待被技术“改造”的落后对象。它拥有长期形成的经验、关系与约束，也背负真实的惯性和代价。转型应先理解，再选择；先局部验证，再决定是否放大；既不迷信过去，也不迷信新技术。
>
> 我相信外部世界先于内部想象，边界是为当前决策服务的临时假设，真正的创新来自消化后的重新组织。完成必须有证据，经验只有改变了下一次行动才算沉淀。

因此，这套方法始终坚持五件事：**先看前例、追踪关系、形成新解、证据验收、跨周期学习**。

## 快速安装

### 方式一：使用 Skills CLI

```bash
npx skills add Kyoyen/agent-skills-for-enterprise-transformation
```

### 方式二：手动安装

```bash
git clone https://github.com/Kyoyen/agent-skills-for-enterprise-transformation.git
mkdir -p ~/.agents/skills
cp -R agent-skills-for-enterprise-transformation/skills/* ~/.agents/skills/
```

也可以只复制某一个 Skill 目录。安装后重新启动或刷新支持 Agent Skills 的客户端。

每个目录都遵循 `SKILL.md` 约定；`references/` 只在需要时加载，`scripts/` 用于适合确定性执行的辅助操作。

## 一般使用场景

| 场景 | 建议路径 |
|---|---|
| 准备引入新的 AI 工具、平台或流程 | `preflight → scale → fusion` |
| 一个跨部门问题越讨论越大 | `scale`，先找临时工作边界 |
| 内部方案与外部最佳实践各有优缺点 | `fusion` |
| 试点或项目准备宣布完成 | `postflight` |
| 每周/月回看人机协作与交付方式 | `retro-insights` |
| 从一次想法走到可持续运行 | `preflight → scale → fusion → 执行 → postflight → retro-insights` |

## 脱敏场景示例

### 示例一：为某多事业部企业引入知识问答

1. `preflight` 先比较平台原生能力、成熟产品、检索增强方案和“不做系统”的替代路径。
2. `scale` 追踪问题与内容责任、权限、更新节奏、反馈闭环的关系，把首轮边界限定为一个知识域和一类高频问题。
3. `fusion` 吸收外部产品的检索体验与内部审核机制，形成适合现有治理条件的方案。
4. 试点后由 `postflight` 核对准确性样本、人工兜底、权限、回滚、Owner 和复查节奏。
5. 连续多个周期后，`retro-insights` 判断哪些做法稳定有效，哪些只是单次偶然。

### 示例二：改造某连锁企业的跨系统协同流程

不先假设“再做一个平台”就是答案。先找已有能力，再沿真实交接、异常、权限和完成证据缩放；把供应商方案、现有系统能力和一线操作方式融合成最小改动；上线前后分别保留验收、恢复和反馈证据。

### 示例三：共享服务团队的月度改进

`retro-insights` 不按会话数、提交数或文档数评价产出，而是寻找多次任务中重复出现的成功模式、摩擦和用户纠正。只有跨任务重复、影响明确或经使用者确认的模式，才进入规则、Skill、检查脚本或运行手册。

更多示例见 [`examples/traditional-enterprise-transformation.md`](examples/traditional-enterprise-transformation.md)。

## 使用边界

- 这些 Skills 提供判断流程，不替代行业专家、业务负责人、合规、法律或安全审查。
- 不要把公开案例直接套用到企业；边界、权限、数据和验收必须重新确认。
- 不要向模型提供无权处理的客户资料、内部日志、账号、密钥或个人信息。
- `retro-insights` 的会话清单脚本默认隐藏本地路径和会话标识；只有明确需要时才选择性开放。
- 关键业务使用前，请在自己的环境中测试和评审。

完整说明见 [`PRIVACY.md`](PRIVACY.md)。

## 仓库结构

```text
.
├── skills/
│   ├── preflight/
│   ├── scale/
│   ├── fusion/
│   ├── postflight/
│   └── retro-insights/
├── examples/
├── CONTRIBUTING.md
├── PRIVACY.md
└── LICENSE
```

## 参与交流

欢迎通过 GitHub Discussions 分享经过脱敏的使用经验，通过 Issues 提交问题或建议，通过 Pull Requests 改进通用方法。提交前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)，不要上传任何组织、客户或个人的可识别信息。

页面结构参考了 [OpenAI Skills](https://github.com/openai/skills)、[Anthropic Skills](https://github.com/anthropics/skills)、[Microsoft Agent Skills](https://github.com/MicrosoftDocs/Agent-Skills) 与 [NVIDIA Skills](https://github.com/NVIDIA/skills) 的公开呈现方式；本仓库的观点、结构、文字和示例均为独立整理。

## License

[MIT License](LICENSE)

## Contact

交流邮箱：[lumon.merrifort@foxmail.com](mailto:lumon.merrifort@foxmail.com)
