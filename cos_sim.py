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
  # 嗜好を定義
  atmosphere_u = { "怖い": 0.03, "美しい": 0.04, "美味しい": 0.06 }
  # イベントaの雰囲気を変数に格納
  atmosphere_a = json_load['はこだてMOMI-Gフェスタ']
  # イベントbの雰囲気を変数に格納
  atmosphere_b = json_load['サル山温泉']
  # イベントcの雰囲気を変数に格納
  atmosphere_c = json_load['五稜星の夢']
  # 比較するラベルを配列に格納
  keys = []
  keys_a = list(atmosphere_a.keys())
  keys_b = list(atmosphere_b.keys())
  keys_c = list(atmosphere_c.keys())
  keys_u = list(atmosphere_u.keys())
  for key_a in keys_a:
    keys.append(key_a)
  for key_b in keys_b:
    keys.append(key_b)
  for key_c in keys_c:
    keys.append(key_c)
  keys = list(set(keys))
  # aとbとuのベクトルを準備
  array_a = []
  array_b = []
  array_c = []
  array_u = []
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
    # cの値準備
    if key in keys_c:
      array_c.append(atmosphere_c.get(key))
    else:
      array_c.append(0)
    # uの値準備
    if key in keys_u:
      array_u.append(atmosphere_u.get(key))
    else:
      array_u.append(0)
  a = np.array(array_a)
  b = np.array(array_b)
  c = np.array(array_c)
  u = np.array(array_u)
  json_file.close()
  return a, b, c, u, atmosphere_u

a, b, c, u, a_u = prepare_vec()
print('ユーザの嗜好: ' + str(a_u))
print('はこだてMOMI-Gフェスタ: ' + str(cos_sim(u, a)))
print('サル山温泉: ' + str(cos_sim(u, b)))
print('五稜星の夢: ' + str(cos_sim(u, c)))