# Thinking Workflow Agent Skills 中文版

本目录包含五个 Skill 的完整中文版。自然语言说明、模板、界面元数据、参考资料和脚本输出均使用中文；Skill 调用名、命令参数、代码关键字和稳定数据字段保持跨语言一致。

## 包含内容

- [`preflight`](skills/preflight/)：行动前检查前例与最简路径。
- [`scale`](skills/scale/)：沿关系缩放并选择可行动边界。
- [`fusion`](skills/fusion/)：消化多个方向，形成自洽的新方案。
- [`postflight`](skills/postflight/)：用证据完成验收、恢复、维护与交接。
- [`retro-insights`](skills/retro-insights/)：从跨周期证据中提炼可验证的改进。

## 安装

在仓库根目录执行：

```bash
mkdir -p ~/.agents/skills
cp -R editions/zh-CN/skills/* ~/.agents/skills/
```

也可以只复制一个 Skill 目录。请勿与英文版同时安装，两套版本使用相同调用名。

返回[仓库中文主页](../../README.md)。
