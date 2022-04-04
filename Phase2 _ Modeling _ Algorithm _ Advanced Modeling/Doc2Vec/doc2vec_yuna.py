# -*- coding: utf-8 -*-
"""Doc2vec_yuna.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c5x_ddPdds9AV5puuji9j_fTeZkPzad1
"""

import time
import os
import pickle
import pandas as pd
import warnings
import numpy as np
import seaborn as sns
from soynlp.tokenizer import RegexTokenizer, LTokenizer, MaxScoreTokenizer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

warnings.filterwarnings("ignore")
# os.chdir("D:\\workspace\\tutorial\\Pro_KPS_Unsturctured\\DATA")

# with open('2018.pickle' , 'rb') as f:
#     data = pickle.load(f)

from google.colab import drive
drive.mount('/content/drive')

# 경로 설정

cd/content/drive/My Drive/tobigs_chatbot/

# Load model

doc_vectorizer = Doc2Vec.load(model_name)

import numpy as np
X = np.array([doc_vectorizer.infer_vector(doc.words) for doc in tagged_train_docs])
y = np.array([int(doc.tags) for doc in tagged_train_docs])

with open('all_Doc2vec_matrix.pickle','wb') as f:
    pickle.dump(X, f, pickle.HIGHEST_PROTOCOL)

import numpy as np

X= np.load('./Doc2Vec_Embedding.npy') # 불러오기

def QnA(x):

  Question = input('질문을 입력하세요.')

  # 코사인 유사도 몇 이상인 것만 가져와라 
  def condition_sorting(x, thresh):
      idx = np.arange(x.size)[x > thresh]
      return idx[np.argsort(x[idx])] 

  # 코사인 유사도 높은 순 index 추출 
  def calculate_cos(matrix, target):
      target_array = doc_vectorizer.infer_vector(target)
      innerproduct = matrix.dot(target_array)
      norm = np.linalg.norm(matrix, axis = 1) * np.linalg.norm(target_array)
      cos = innerproduct / norm # 코사인 유사도 계산 
      index = condition_sorting(cos, 0.4)[::-1][:200] # 유사도 0.4이상인 것 
      return index
  
  # # khaii 설정 
  # !git clone https://github.com/kakao/khaiii.git
  # !pip install cmake
  # !mkdir build
  # !cd build && cmake /content/khaiii
  # !cd /content/build/ && make all
  # !cd /content/build/ && make resource
  # !cd /content/build && make install
  # !cd /content/build && make package_python
  # !pip install /content/build/package_python
 
  # khaii 엮기 
  from khaiii import KhaiiiApi
  api = KhaiiiApi()

  new_question = []
  for word in api.analyze(Question): 
      for morph in word.morphs:
          new_question.append(morph.lex)

  # '상위 5 Answer :\n', 
  return  '상위 5 Answer :', df.iloc[calculate_cos(X, new_question)[:5]]['Answer'].tolist()