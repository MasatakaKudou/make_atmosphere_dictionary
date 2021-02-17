import json

class DeleteBelowThreshold:
  # 雰囲気辞書から閾値以下の雰囲気を削除
  def read_atmosphere_dict(self, en_noun, ja_noun):
    # ファイル開く
    json_file = open(f'{en_noun}/{en_noun}.json', 'r')
    # ファイルの読み込み
    json_load = json.load(json_file)
    # 閾値以上の雰囲気を格納する辞書を準備
    new_dict = {}
    # 閾値の削除
    atomosphere_dict = json_load[ja_noun]
    for atomosphere in atomosphere_dict:
      value = atomosphere_dict[atomosphere]
      if value >= 0.03:
        new_dict[atomosphere] = value
    # ファイルを閉じる
    json_file.close()
    return new_dict

  # 雰囲気辞書のkeyに名詞を定義
  def define_noun(self, new_dict, noun):
    # 名詞をkeyとするために新しい辞書を準備
    new_atmosphere_dict = {}
    # 名詞に対する雰囲気をvalueとして登録
    new_atmosphere_dict[noun] = new_dict
    return new_atmosphere_dict

  # 新しい雰囲気辞書を登録
  def register_new_atmosphere_dict(self, new_atmosphere_dict, noun):
    # ファイル開く
    json_file = open(f'{noun}/{noun}_d.json', 'w')
    # ファイルに書き込み
    json.dump(new_atmosphere_dict, json_file, indent=2, ensure_ascii=False)
    # ファイルを閉じる
    json_file.close()