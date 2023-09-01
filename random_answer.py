import csv
import random


def get_answer():
    "获得答案"
    # 打开CSV文件
    with open('database.csv', 'r', encoding='utf-8') as file:
        # 创建CSV读取器
        reader = csv.reader(file)

        # 记录行数
        line_count = sum(1 for row in reader)

        # 随机选择一行的行号
        random_line_number = random.randint(1, line_count)

        # 重新将文件指针定位到文件开头
        file.seek(0)

        # 逐行读取CSV文件内容，直到随机选择的行
        for line_number, row in enumerate(reader, start=1):
            if line_number == random_line_number:
                page, en, zh = row[:3] 
                answer = f"n{en}\n{zh}"

                #print(answer)
                #print(f"页数：{page}\n{en}\n{zh}")
                #print(f"页数{page}")
                #print(en)
                #print(zh)
                break
    return answer

# get_answer()

