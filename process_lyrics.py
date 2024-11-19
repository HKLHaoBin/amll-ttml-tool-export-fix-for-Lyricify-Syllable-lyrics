import os
import json
import re
import requests

def process_line(line):
    # 删除形如 "(0,0)" 的模式
    line = re.sub(r'\(0,0\)', '', line)
    # 定义匹配模式，找到字符、左括号、内容、右括号，以及右括号后的空格
    pattern = re.compile(r'(.)\((.*?)\)(\s*)')
    idx = 0
    while idx < len(line):
        match = pattern.search(line, idx)
        if not match:
            break
        # 获取匹配的各个部分
        before_char = match.group(1)
        inside_paren = match.group(2)
        spaces_after = match.group(3)
        start, end = match.span()

        # 检查右括号后是否有空格
        if spaces_after:
            # 移除右括号后的空格
            line = line[:match.end(2)+1] + line[end:]
            # 在左括号前添加空格
            insert_pos = match.start(2) - 1
            # 防止重复添加空格
            if line[insert_pos] != ' ':
                line = line[:insert_pos+1] + ' ' + line[insert_pos+1:]
            # 更新索引位置，继续查找下一个匹配项
            idx = match.start() + 1  # 移动到当前匹配的下一个字符
        else:
            idx = match.end()  # 如果没有空格，跳过当前匹配

        # 匹配并替换 "( " 为 " ("
        line = re.sub(r'\(\s+', ' (', line)


    return line

def process_text(text):
    lines = text.strip().split('\n')
    processed_lines = [process_line(line) for line in lines]
    return '\n'.join(processed_lines)

def main():
    # 读取事件数据
    event_path = os.environ['GITHUB_EVENT_PATH']
    with open(event_path, 'r') as f:
        event = json.load(f)
    issue = event['issue']
    issue_number = issue['number']
    issue_body = issue['body']
    # 提取需要纠错的歌词，假设歌词在 ``` 中
    code_blocks = re.findall(r'```(.*?)```', issue_body, re.DOTALL)
    if not code_blocks:
        print("未在 issue 中找到歌词。")
        return
    lyrics = code_blocks[0]
    # 处理歌词
    processed_lyrics = process_text(lyrics)

    # 按行分割文本
    lines = processed_lyrics.strip().split('\n')

    processed_lyrics = ""

    for s in lines:
        #print("----------------------------------------")
        #print("原始行：", s)
        # 修改正则表达式，匹配可能不存在的单词
        matches = list(re.finditer(r'\)\s*(\w*)\s*\(', s))
        #print("匹配结果：", matches)
        if matches:
            last_match = matches[-1]
            word = last_match.group(1)
            #print("匹配到的单词：", word)
            start, end = last_match.span()
            #print("匹配位置：", start, end)
            # 去掉匹配模式中的空格
            s = s[:start] + ')' + word + '(' + s[end:]
        #print("修改后：", s)
        print(s)
        processed_lyrics += s

    # 在 issue 中添加评论
    token = os.environ['GITHUB_TOKEN']
    repo = os.environ['GITHUB_REPOSITORY']
    url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/comments'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    comment_body = f"处理后的歌词：\n\n```{processed_lyrics}```"
    data = {'body': comment_body}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("成功发布评论。")
    else:
        print(f"发布评论失败，状态码：{response.status_code}")
        print(response.text)

if __name__ == '__main__':
    main()
