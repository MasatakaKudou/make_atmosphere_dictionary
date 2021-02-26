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

text = '冬の五稜郭公園の堀が約2000個の電球で彩られ、公園の周遊路を散策しながら楽しめる。堀の水が凍って雪が一面に積もると、柔らかい光に照らし出されて幻想的。数々の歴史の舞台となった特別史跡五稜郭跡は、星形にめぐらされた堀が特徴的。その堀を冬の間イルミネーションでふちどり、幻想的に浮かび上がらせるのが「五稜星の夢（ほしのゆめ）」です。点灯時間は日没から20時まで。堀の外周に設けられた歩行者専用道路（一周約1.8km、周回する場合の所要時間は30～40分）を散策すると、冬の初めの堀が凍るまでの期間は、水面に光が反射して揺らめき、華やかな雰囲気。堀に氷が張ると、スケートリンクのように輝きが増します。さらに、氷の上に雪が積もると一面真っ白になり、幽玄の世界に。時期や時間、天気、雪の有無で見え方が違うので、どんな景色に出会えるかはお楽しみです。'

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
event_atmosphere_dict['五稜星の夢'] = event_atmosphere

new_json_file = open('event_atmosphere_1.json', 'w')
json.dump(event_atmosphere_dict, new_json_file, indent=2, ensure_ascii=False)
new_json_file.close()