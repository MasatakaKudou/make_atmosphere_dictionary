import numpy as np
import json

# コサイン類似度の計算
def cos_sim(v1, v2):
  return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# ベクトルの準備
def prepare_vec():
  # 紅葉の雰囲気辞書を読み込む
  json_file_koyo = open('koyo/koyo_d.json', 'r')
  json_load_koyo = json.load(json_file_koyo)
  atmosphere_koyo = json_load_koyo['紅葉']
  # 随一の雰囲気辞書を読み込む
  json_file_zuiichi = open('zuiichi/zuiichi_d.json', 'r')
  json_load_zuiichi = json.load(json_file_zuiichi)
  atmosphere_zuiichi = json_load_zuiichi['随一']
  # 比較するラベルを配列に格納
  keys = []
  keys_koyo = list(atmosphere_koyo.keys())
  keys_zuiichi = list(atmosphere_zuiichi.keys())
  for key_x in keys_koyo:
    keys.append(key_x)
  for key_y in keys_zuiichi:
    keys.append(key_y)
  keys = set(keys)
  # XとYのベクトルを準備
  X_array = []
  Y_array = []
  for key in keys:
    # Xの値準備
    if key in keys_koyo:
      X_array.append(atmosphere_koyo.get(key))
    else:
      X_array.append(0)
    # Yの値準備
    if key in keys_zuiichi:
      Y_array.append(atmosphere_zuiichi.get(key))
    else:
      Y_array.append(0)
  X = np.array(X_array)
  Y = np.array(Y_array)
  json_file_koyo.close()
  json_file_zuiichi.close()
  return X, Y

X, Y = prepare_vec()
print(cos_sim(X, Y))