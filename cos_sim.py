import numpy as np
import json

# コサイン類似度の計算
def cos_sim(v1, v2):
  return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# ベクトルの準備
def prepare_vec():
  # 雰囲気辞書を読み込む
  json_file = open('event_atmosphere.json', 'r')
  json_load = json.load(json_file)
  # イベント1の雰囲気を変数に格納
  atmosphere_a = json_load['はこだてMOMI-Gフェスタ']
  # イベント2の雰囲気辞書を読み込む
  atmosphere_b = json_load['サル山温泉']
  # 比較するラベルを配列に格納
  keys = []
  keys_a = list(atmosphere_a.keys())
  keys_b = list(atmosphere_b.keys())
  for key_a in keys_a:
    keys.append(key_a)
  for key_b in keys_b:
    keys.append(key_b)
  keys = list(set(keys))
  # aとbのベクトルを準備
  array_a = []
  array_b = []
  for key in keys:
    # aの値準備
    if key in keys_a:
      array_a.append(atmosphere_a.get(key))
    else:
      array_a.append(0)
    # bの値準備
    if key in keys_b:
      array_b.append(atmosphere_b.get(key))
    else:
      array_b.append(0)
    print(key)
  a = np.array(array_a)
  b = np.array(array_b)
  json_file.close()
  return a, b

a, b = prepare_vec()
print(cos_sim(a, b))