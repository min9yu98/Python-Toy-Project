from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence, PathLineSentences

sentences = LineSentence('C:/Users/kmkkm/Desktop/ChosunJoongang_total_pos.txt')
model = Word2Vec(sentences, vector_size=300, sg=0, workers=4)

model_result = model.wv.most_similar("코로나", topn=100) # Word Embedding Similiarity
for i in range(len(model_result)):
  print(model_result[i])
  print('\n')


with open('C:/Users/kmkkm/Desktop/ChosunJoongang_total_wv_most_similar_100.txt', 'a', encoding='UTF-8') as f: # txt로 저장
  for i in range(len(model_result)):
      f.write(model_result[i][0] + '  ' + str(model_result[i][1]) + '\n')