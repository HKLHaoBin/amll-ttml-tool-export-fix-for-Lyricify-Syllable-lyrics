# 拯救你的歌词！！！

## **仓库名称**: 处理 amll-ttml-tool 导出为Lyricify Syllable 歌词时的错误纠正

# [点击这里使用本工具](https://github.com/HKLHaoBin/amll-ttml-tool-export-fix-for-Lyricify-Syllable-lyrics/issues/new/choose)

[或者使用更加可靠的 ttml_to_lys ](https://github.com/HKLHaoBin/ttml_to_lys)


**描述**:  
本仓库旨在提供一种自动化工具，用于纠正从 `amll-ttml-tool` 导出为 `Lyricify Syllable` 格式的歌词文件时可能出现的格式错误。通过解析和调整文本内容，确保歌词数据在语法和格式上符合预期。

### 功能特色
- **括号处理**: 自动检测并移除不必要的 `(0,0)` 模式。
- **格式优化**: 在特定的括号内容前后调整空格位置，确保歌词格式正确。

### 使用方法
1. 将需要纠错的 `Lyricify Syllable` 歌词提交到 `issues` 中。
2. 运行脚本，脚本会自动对每行歌词进行格式化处理。
3. 输出处理后的歌词，修复常见的格式问题。

### 适用场景
- 修复导出工具产生的语法或排版问题。
- 优化歌词文件格式以便更好地兼容其他系统。
- 自动化处理大批量歌词文件的排版修正。

### 使用说明书

此脚本用于处理 GitHub issue 中的歌词文本，主要实现以下功能：

1. **删除特定模式**：删除所有类似 `(0,0)` 的内容。
2. **格式化歌词**：调整歌词中的括号空格，确保语法一致。
3. **检查并修改匹配项**：在括号之间的空格处理和字词调整。
4. **发布修改结果**：将修改后的歌词文本作为评论发布到 GitHub issue。

### 前提条件

- **GitHub 环境**：脚本假定在 GitHub Actions 中运行，且需要获取相关的事件数据和认证 Token。
- **环境变量**：
  - `GITHUB_EVENT_PATH`：GitHub Actions 提供的路径，用于获取当前事件的数据。
  - `GITHUB_TOKEN`：GitHub 认证 token，需具备 issue 评论权限。
  - `GITHUB_REPOSITORY`：GitHub 仓库的完整名称（例如 `owner/repo`）。
  
### 功能步骤

1. **读取事件数据**：从 `GITHUB_EVENT_PATH` 中加载 GitHub 事件数据。
2. **提取歌词**：从 issue 的正文中提取包含在 ``` 中的歌词文本。
3. **处理歌词**：
   - 删除不必要的 `(0,0)` 内容。
   - 调整括号与文本之间的空格，确保一致性。
   - 对特定模式进行修改，如括号中的词。
4. **发布评论**：处理完成的歌词将通过 GitHub API 作为评论发布到当前 issue。

### 如何运行

1. **环境准备**：确保 GitHub Actions 环境配置好 `GITHUB_EVENT_PATH`、`GITHUB_TOKEN` 和 `GITHUB_REPOSITORY` 环境变量。
2. **启动脚本**：运行脚本时，确保事件数据和环境变量配置正确，脚本将自动处理歌词并发布评论。

### 运行示例

假设当前 `issue` 中有一段格式不规范的歌词，脚本将按如下方式操作：

- 输入歌词：
  ```
  [0]像(10767,653) (0,0)从(12073,289)不(12363,289)认(12652,434)识(13086,596)你(13682,543)
  ```

- 处理后输出：
  ```
  [0]像 (10767,653)从(12073,289)不(12363,289)认(12652,434)识(13086,596)你(13682,543)
  ```

### 错误处理

- **未找到歌词**：若在 issue 中未找到符合格式的歌词（没有 ``` 包围的部分），脚本会打印“未在 issue 中找到歌词”并退出。
- **评论发布失败**：若脚本无法成功发布评论（如 token 权限不足或网络问题），会打印错误信息。

### 注意事项

- **字符匹配**：本脚本使用正则表达式来识别和处理特定模式，可能会对其他不符合预期的文本产生影响。
- **GitHub Token**：确保 `GITHUB_TOKEN` 拥有评论权限，并且没有过期。

### 版权与免责声明

此脚本由开发者提供，旨在自动化处理 GitHub issue 中的歌词文本。使用时请遵守相关 GitHub 使用条款。

欢迎贡献代码、报告问题或提出改进建议！
