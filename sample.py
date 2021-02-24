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

text = '12月から春の大型連休最終日まで、温泉にのんびりとつかるニホンザルの愛らしい姿が見られる。函館空港近くの湯の川温泉・函館市熱帯植物園で。園内に温室、足湯もあり。函館の冬の風物詩のひとつ、函館市熱帯植物園で温泉につかるニホンザル。サル山のプールに温泉を引き入れるのは、12月1日から春の大型連休最終日までの期間限定。野外の寒さや風雪をしのぐため、湯につかって温まるサルたちの愛くるしい表情やしぐさは、どこかユーモラスでかわいらしいと評判です。開園中はいつでも間近で観察できます（要入園料）。もっとコミュニケーションをとりたいなら、案内所で専用の「サルのエサ（100円）」を買って、柵越しにエサやり体験をすることも可能。不定期に、りんごなどの好物をプレゼントすることのできる特別イベントも企画されています。寒くなったら園内の足湯を利用したり、冬でも暖かい温室へ。北国の冬景色から一転、珍しい南国の植物が植えられた温室内は快適、休憩スペースも設けられています。'

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

new_json_file = open('event_atmosphere_1.json', 'w')
json.dump(event_atmosphere_dict, new_json_file, indent=2, ensure_ascii=False)
new_json_file.close()