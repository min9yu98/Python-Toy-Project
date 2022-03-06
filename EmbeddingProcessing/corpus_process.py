from konlpy.tag import Okt
import re

with open('저장경로', 'a', encoding='utf-8') as file:  # 입력
    for i in range(2):
        for j in range(1, 13):
            path1 = '불러올 경로'
            f = open(path1, 'r', encoding='utf-8')
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                file.write(line + "\n")
            f.close()


