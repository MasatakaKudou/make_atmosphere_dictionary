import numpy as np
import itertools
from fractions import Fraction
import csv
import json
import analysis as mecab
from collections import Counter, defaultdict

class CalcCoOccurence:
    # words_listの作成, キーワード毎の要素数をカウント
    def make_words_list(self, tweet_list):
        # wordsを格納するリスト
        words_list = []
        for tweet in tweet_list:
            # 形容詞のリストを取得
            adjective_words = mecab.wakati_text(tweet[1])
            # 空配列以外は以下の処理を実行
            if adjective_words:
                # 配列に格納
                words_list.append(adjective_words)
        return words_list

    # wordのpairを作成
    def make_pair_list(self, words_list):
        pair_list = []
        # 配列の要素数が2以上の時だけ単語のペアを作成
        for words in words_list:
            for word in words:
                pair_list.append(word)
        return pair_list

    # 名詞と形容詞と共起度のリストを作成
    def make_atmosphere_dict(self, pair_list):
        atmosphere_dict = {}
        sub_dict = {}
        cnt_pairs = Counter(pair_list)
        for cnt_pair in cnt_pairs:
            co_occurrence = cnt_pairs[cnt_pair] / 500
            sub_dict[cnt_pair] = co_occurrence
        #     # デバック用
        #     # print(f'ペア : {cnt_pair}')
        #     # print(f'積集合: {cnt_pairs[cnt_pair]}')
        #     # print(f'和集合: 50')
        #     # print(f'共起度: {cnt_pairs[cnt_pair]/50}')
        atmosphere_dict['フェスタ'] = sub_dict
        return atmosphere_dict


# csvファイルを開く
csv_file = open('festa/festa.csv', 'r')
# csvファイルを読み込む
csv_content = csv.reader(csv_file, doublequote=False)
# headerをスキップ
next(csv_content)
# リストに格納(この後何回も使えるようになる)
tweet_list = []
for row in csv_content:
    tweet_list.append(row)
# csvファイル閉じる
csv_file.close()

# インスタンス作成
instance = CalcCoOccurence()
# 返り値1:行毎の単語リストを取得, 返り値2:キーワード毎のtweet数を取得
words_list = instance.make_words_list(tweet_list)
# 行毎の単語ペアを作成
pair_list = instance.make_pair_list(words_list)
# 名詞と形容詞と共起度のリストを作成
atmosphere_dict = instance.make_atmosphere_dict(pair_list)

# ファイル開く
json_file = open('festa/festa.json', 'w')
# ファイルに書き込み
json.dump(atmosphere_dict, json_file, indent=2, ensure_ascii=False)
# ファイルを閉じる
json_file.close()