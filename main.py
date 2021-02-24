import json
from pykakasi import kakasi

import getTweets as g # ツイートを収集
import calc as c # 名詞・形容詞・共起度をセットで辞書に登録
import deleteBelowThreshold as d # 閾値以下削除
import plot as p # グラフを描画

### 変数・定数を定義 ###
ja_noun = ''
en_noun = ''
SEARCH_COUNT = 100
# kakasiセット
kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

for noun in ['寒さ', '温室', 'しぐさ', '湯の川温泉', 'イベント', 'コミュニケーション', '足湯', '表情', '野外', '春の', '特別', '最終日', '一転', '不定期', 'プール', '利用', 'どこか', '好物']:
  ### 日本語をローマ字に変更 ###
  ja_noun = noun
  en_noun = conv.do(ja_noun)

  ### ツイートを収集 ###
  # インスタンス作成
  g_instance = g.GetTweets()
  # データを貯めるディレクトリを生成
  g_instance.make_dir(en_noun)
  # ツイートを収集
  for day in list(range(19, 24)):
      params = {
        'since': f'2021-02-{day}_00:00:00_JST',
        'until': f'2021-02-{day}_23:59:59_JST',
        'exclude': 'retweets',
        'count': SEARCH_COUNT,
        'q': ja_noun
      }
      g_instance.get_tweets(params, en_noun)

  ### 名詞・形容詞・共起度をセットで辞書に登録 ###
  # インスタンス作成
  c_instance = c.CalcCoOccurence()
  # ツイートデータ読み込み
  tweet_list = c_instance.read_tweets(en_noun)
  # 行毎の単語リストを取得
  words_list = c_instance.make_words_list(tweet_list)
  # 行毎の単語ペアを作成
  pair_list = c_instance.make_pair_list(words_list)
  # 名詞と形容詞と共起度のリストを作成
  atmosphere_dict = c_instance.make_atmosphere_dict(pair_list, ja_noun)
  # 雰囲気辞書に登録
  c_instance.register_atmosphere_dict(atmosphere_dict, en_noun)

  ### 閾値以下の雰囲気を削除 ###
  # インスタンス作成
  d_instance = d.DeleteBelowThreshold()
  # 雰囲気辞書から閾値以下の雰囲気を削除
  new_atmosphere_sub_dict = d_instance.read_atmosphere_dict(en_noun, ja_noun)
  # 雰囲気辞書のkeyに名詞を定義
  new_atmosphere_dict = d_instance.define_noun(new_atmosphere_sub_dict, ja_noun)
  # 新しい雰囲気辞書を登録
  d_instance.register_new_atmosphere_dict(new_atmosphere_dict, en_noun)

  ### 図を描画 ###
  # インスタンス作成
  p_instance = p.Plot()
  # 図を描画
  p_instance.plot_atmosphere(en_noun, ja_noun)