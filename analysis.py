# 形態素解析に使う
import MeCab
# ディレクトリからファイル名を取得するのに使う
import glob
import os
import json

# MeCabの準備
mecab = MeCab.Tagger('-d /Users/kudoumasataka/my_local/homebrew/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')

# 取り出したい品詞
select_conditions = ['形容詞']

# 形態素解析
def wakati_text(text):
  # 分けてノードごとにする
  node = mecab.parseToNode(text)
  words = []
  adjective_words = []
  
  while node:
    # 単語の原型を取得
    word = node.feature.split(",")[6]
    # 品詞
    pos = node.feature.split(',')[0]
    # もし品詞が条件と一致してたら
    if pos in select_conditions:
      adjective_words.append(word)
    node = node.next

  return adjective_words