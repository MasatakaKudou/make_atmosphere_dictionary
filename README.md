## ファイル説明
* atmosphere/
  * どう言うものか
    * 雰囲気辞書に使っていたデータを溜めている
  * データ構成
    * noun/
      * noun.csv / ツイートデータ
      * noun.json / 名詞に対する雰囲気辞書
      * noun_d.json / 閾値0.03以下を削除した，名詞に対する雰囲気辞書
      * 名詞.png / 閾値0.03以下を削除した，名詞に対する雰囲気辞書をグラフ化
* analysis.py
  * 形態素解析して形容詞を取り出す
* atmosphere.json
  * イベント5件に対しての雰囲気辞書
* calc.py
  * 共起度を算出する
* config.py
  * APIにアクセスするためのキーやトークンなどを所持
* cos_sim_sample.py
  * 類似度を算出できるか試した
* cos_sim.py
  * イベント5件と嗜好との類似度を算出
* deleteBelowThreshold.py
  * 閾値0.03以下の削除
* deleteDuplicate.py
  * 重複削除
* event_atmosphere.json
  * イベント5件から抽出された雰囲気
* getTweets.py
  * ツイートの収集
* main.py
  * ツイート取得，雰囲気辞書の生成，閾値の削除，グラフに描画までを一括で行う
* plot.py
  * グラフを描画
* sample.py
  * 形態素解析して名詞を取り出す
  * イベント1件に対しての雰囲気をjsonで出力
  * 関数で分けたりしてないから，コメントアウトして使用
* twitterSession.py
  * OAuth認証
