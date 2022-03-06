from konlpy.tag import Okt
import re

with open('C:/Users/kmkkm/Desktop/SBS_total.txt', 'a', encoding='utf-8') as file:  # 입력
    for i in range(2):
        for j in range(1, 13):
            path1 = 'C:/Users/kmkkm/Desktop/sbs/202' + str(i) + '_' + str(j) + '_sbs.txt'
            f = open(path1, 'r', encoding='utf-8')
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                file.write(line + "\n")
            f.close()


