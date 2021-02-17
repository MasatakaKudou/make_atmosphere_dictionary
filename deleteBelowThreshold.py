import json

# ファイル開く
json_file = open('festa/festa.json', 'r')
# ファイルの読み込み
json_load = json.load(json_file)
# 入れ物
new_dict = {}
# 閾値の削除
atomosphere_dict = json_load['フェスタ']
for atomosphere in atomosphere_dict:
  value = atomosphere_dict[atomosphere]
  if value >= 0.03:
    new_dict[atomosphere] = value
# ファイルを閉じる
json_file.close()

a = {}
a['フェスタ'] = new_dict

# # ファイル開く
new = open('festa/festa_d.json', 'w')
# # ファイルに書き込み
json.dump(a, new, indent=2, ensure_ascii=False)
# # ファイルを閉じる
json_file.close()