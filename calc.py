import csv
import json
import analysis as mecab
from collections import Counter

class CalcCoOccurence:
    # ツイートデータの読み込み
    def read_tweets(self, noun):
        # csvファイルを開く
        csv_file = open(f'{noun}/{noun}.csv', 'r')
        # csvファイルを読み込む
        csv_content = csv.reader(csv_file, doublequote=False)
        # リストを準備(ファイルを開き続けるとメモリを食うから)
        tweet_list = []
        # csvを一行ずつtweet_listに格納
        for row in csv_content:
            tweet_list.append(row)
        # csvファイル閉じる
        csv_file.close()
        return tweet_list
    
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
        for words in words_list:
            for word in words:
                pair_list.append(word)
        return pair_list

    # 名詞と形容詞と共起度のリストを作成
    def make_atmosphere_dict(self, pair_list, noun):
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
        atmosphere_dict[noun] = sub_dict
        return atmosphere_dict
    
    # 名詞と形容詞と共起度をセットで登録
    def register_atmosphere_dict(self, atmosphere_dict, noun):
        json_file = open(f'{noun}/{noun}.json', 'w')
        json.dump(atmosphere_dict, json_file, indent=2, ensure_ascii=False)
        json_file.close()