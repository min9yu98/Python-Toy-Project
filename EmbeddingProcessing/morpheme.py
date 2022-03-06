from konlpy.tag import Okt
import re
from tqdm import tqdm

okt = Okt()
special = re.compile(r'[^ A-Za-z0-9가-힣+]')
concat = []
corpus = []

text_file = '불러올 경로'
f = open(text_file, 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
  corpus.append(line)
f.close()
# print(corpus[-1])

clean_corpus = []
for text in corpus:
  clean_corpus.append([special.sub('', text)])

token_corpus = []
processing = tqdm(clean_corpus)
for text in processing:
  token_corpus.append(okt.morphs(text[0]))
pos_text = []
pos_text.append(token_corpus)

# print(pos_text[0][-1])
with open('저장할 ', 'a', encoding='utf-8') as f:
  for j in range(len(pos_text[0])):
    t = ' '.join(pos_text[0][j])
    f.write(t + '\n')
