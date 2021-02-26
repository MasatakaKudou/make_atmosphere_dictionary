# coding: UTF-8

# 形態素解析に使う
import MeCab
import re
import json

# MeCabの準備
mecab = MeCab.Tagger('-d /Users/kudoumasataka/my_local/homebrew/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')

# 取り出したい品詞
select_conditions = ['名詞']

text = 'ロマンチックな雰囲気のあるベイエリアの運河に、期間限定の神社が出現。オリジナルの絵馬を購入して、願いをかけることができる。初詣、合格祈願などにどうぞ。金森赤レンガ倉庫にある運河に、1月1日～2月28日限定で神社が出現します。16～22時にはライトアップされ、厳かな雰囲気に。赤い鳥居の奥に浮かぶ神社は、函館総鎮守・函館八幡宮から魂入れを受けた由緒あるもの。金森洋物館・BAYはこだての各インフォメーションで絵馬（500円）を購入し、掛所に結べば願いがかなうかもしれません。絵馬を購入したかたには、函館八幡宮で祈祷した御福銭が進呈されます。期間終了後、掛所の絵馬は函館八幡宮に奉納されます。初詣や合格祈願、良縁祈願などにいかがでしょうか。'

# 形態素解析
def wakati_text(text):
  # 分けてノードごとにする
  node = mecab.parseToNode(text)
  words = []
  adjective_words = []
  
  while node:
    # 単語の原型を取得
    word = node.feature.split(",")[6]
    # FESTA!!はフェスタに変更
    if word == 'FESTA!!':
      word = 'フェスタ'
    # 品詞
    pos = node.feature.split(',')[0]
    # 名詞の種類
    subtype = node.feature.split(',')[1]
    # もし品詞が条件と一致してたら
    if pos in select_conditions:
      if subtype not in ['非自立', '接尾', '副詞可能']:
        if not re.match(r"\d+(\w|[亜-熙])", word):
          adjective_words.append(word)
    node = node.next
  return adjective_words

noun_list = list(set(wakati_text(text)))
print(noun_list)
# event_atmosphere = {}
# event_atmosphere_dict = {}
# json_file = open('atmosphere.json', 'r')
# json_load = json.load(json_file)
# for noun in noun_list:
#   if noun in json_load.keys():
#     for atmosphere_key in json_load[noun].keys():
#       if atmosphere_key not in event_atmosphere.keys():
#         event_atmosphere[atmosphere_key] = json_load[noun][atmosphere_key]
#       else:
#         if json_load[noun][atmosphere_key] > event_atmosphere[atmosphere_key]:
#           event_atmosphere[atmosphere_key] = json_load[noun][atmosphere_key]
# json_file.close()
# event_atmosphere_dict['市立函館博物館収蔵資料展'] = event_atmosphere

# new_json_file = open('event_atmosphere_1.json', 'w')
# json.dump(event_atmosphere_dict, new_json_file, indent=2, ensure_ascii=False)
# new_json_file.close()