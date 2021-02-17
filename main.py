import json

import calc as c # 名詞・形容詞・共起度をセットで辞書に登録
import deleteBelowThreshold as d # 閾値以下削除
import plot as p # グラフを描画

### 名詞を定義 ###
ja_noun = 'テスト'
en_noun = 'test'

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