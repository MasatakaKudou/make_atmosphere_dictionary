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

text = '紅葉の名所として知られる香雪園のイベント。夜間ライトアップが人気で、約100メートルのカエデ並木が光に照らし出されて幻想的。「はこだてMOMI-G（もみじ）フェスタ」は、函館随一の紅葉の名所である香雪園（見晴公園）で行われるイベントです。期間中は、約100メートル続くカエデ並木を毎日ライトアップ。園内は幻想的な雰囲気に包まれます（16～21時）。香雪園は、明治時代の豪商の別荘だったもので、現在は函館市の公園として市民に親しまれています（北海道で唯一の国指定文化財庭園）。広大な敷地には約150種類の樹木が植栽され、見どころの多い日本式庭園を楽しめるよう、散策路が整備されています。函館空港や湯の川温泉から車で約10分の距離。函館駅からの路線バスがあります。ライトアップの時間帯は冷え込むので、暖かい服装でお出かけください。'

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
event_atmosphere_dict['はこだてMOMI-Gフェスタ'] = event_atmosphere

new_json_file = open('event_atmosphere.json', 'w')
json.dump(event_atmosphere_dict, new_json_file, indent=2, ensure_ascii=False)
new_json_file.close()