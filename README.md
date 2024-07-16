#书生大模型
  [实战营](https://github.com/InternLM/Tutorial)
闯关任务
![闯关任务](https://github.com/user-attachments/assets/ba26e9e8-a6ac-42ac-9e89-67b5b1bc3a5e)

## L0-Linux任务
过程结果参考笔记：[L0-Linux](https://blog.csdn.net/LeLe_88888888/article/details/140351400?spm=1001.2014.3001.5502)
1. 本地VSCode中通过SSH连接远程开发机
   连接成功后创建虚拟环境
   `conda create -n your_env_name python==3.10 -y`
2. 完成SSH连接与端口映射并运行 hello_world.py
   激活环境并运行py文件
   ```
   conda activate your_env_name
   python hello_world.py
   ```

## L0-python任务
结果参考笔记：[L0-python](https://blog.csdn.net/LeLe_88888888/article/details/140438701?spm=1001.2014.3001.5502)
1. 实现一个word_count函数
   
```
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
   ```
2. Vscode连接InternStudio debug
  
```
python -m pdb word_count.py
  //(Pdb) 会自动停在第一行，等待调试
```
  
