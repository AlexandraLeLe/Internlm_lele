import re
from collections import Counter

def wordcount(text):
    # 用正则表达式替换标点符号为空格
    cleaned_text = re.sub(r'[^\w\s]', ' ', text)
    # 将所有单词转换为小写
    cleaned_text = cleaned_text.lower()
    # 分割字符串为单词列表
    words = cleaned_text.split()
    # 使用Counter计算每个单词出现的次数
    word_count = Counter(words)
    return dict(word_count)


text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

output = wordcount(text)
print(output)
