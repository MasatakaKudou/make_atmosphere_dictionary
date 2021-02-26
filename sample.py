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

text = '函館公園内にある市立函館博物館に収蔵されている、縄文時代の土器や土偶などを展示。世界遺産に推薦されている「北海道・北東北の縄文遺跡群」の紹介コーナーも。函館公園内の市立函館博物館で、函館市内で発掘・収集された縄文の遺物が展示されています。時代の変遷がみられる土器をはじめ、バラエティ豊かな土偶、鹿の角で作られた角偶、愛らしいフォルムの動物土偶など、さまざまな遺物を見ることができます。函館市の史跡である大船遺跡・垣ノ島遺跡を含む「北海道・北東北の縄文遺跡群」は、ユネスコ世界遺産に推薦されており、構成する17の遺跡の紹介コーナーもあります。このほか、市立函館博物館では、常設展「はこだての歩み」（通史展示）、収蔵資料展「箱館戦争」も開かれています。'

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
# print(noun_list)
event_atmosphere = {}
event_atmosphere_dict = {}
json_file = open('atmosphere.json', 'r')
json_load = json.load(json_file)
for noun in noun_list:
  if noun in json_load.keys():
    for atmosphere_key in json_load[noun].keys():
      if atmosphere_key not in event_atmosphere.keys():
        event_atmosphere[atmosphere_key] = json_load[noun][atmosphere_key]
      else:
        if json_load[noun][atmosphere_key] > event_atmosphere[atmosphere_key]:
          event_atmosphere[atmosphere_key] = json_load[noun][atmosphere_key]
json_file.close()
event_atmosphere_dict['市立函館博物館収蔵資料展'] = event_atmosphere

new_json_file = open('event_atmosphere_1.json', 'w')
json.dump(event_atmosphere_dict, new_json_file, indent=2, ensure_ascii=False)
new_json_file.close()