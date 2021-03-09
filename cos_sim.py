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
  # 嗜好を定義(実験ではここを手動で変化させる)
  atmosphere_u = json_load['はこだてMOMI-Gフェスタ']
  # イベントaの雰囲気を変数に格納
  atmosphere_a = json_load['はこだてMOMI-Gフェスタ']
  # イベントbの雰囲気を変数に格納
  atmosphere_b = json_load['サル山温泉']
  # イベントcの雰囲気を変数に格納
  atmosphere_c = json_load['五稜星の夢']
  # イベントdの雰囲気を変数に格納
  atmosphere_d = json_load['市立函館博物館収蔵資料展']
  # イベントeの雰囲気を変数に格納
  atmosphere_e = json_load['冬の金森神社に願いごと']
  # 比較するラベルを配列に格納
  keys = []
  keys_a = list(atmosphere_a.keys())
  keys_b = list(atmosphere_b.keys())
  keys_c = list(atmosphere_c.keys())
  keys_d = list(atmosphere_d.keys())
  keys_e = list(atmosphere_e.keys())
  keys_u = list(atmosphere_u.keys())
  for key_a in keys_a:
    keys.append(key_a)
  for key_b in keys_b:
    keys.append(key_b)
  for key_c in keys_c:
    keys.append(key_c)
  for key_d in keys_d:
    keys.append(key_d)
  for key_e in keys_e:
    keys.append(key_e)
  keys = list(set(keys))
  # aとbとuのベクトルを準備
  array_a = []
  array_b = []
  array_c = []
  array_d = []
  array_e = []
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
    # dの値準備
    if key in keys_d:
      array_d.append(atmosphere_d.get(key))
    else:
      array_d.append(0)
    # eの値準備
    if key in keys_e:
      array_e.append(atmosphere_e.get(key))
    else:
      array_e.append(0)
    # uの値準備
    if key in keys_u:
      array_u.append(atmosphere_u.get(key))
    else:
      array_u.append(0)
  a = np.array(array_a)
  b = np.array(array_b)
  c = np.array(array_c)
  d = np.array(array_d)
  e = np.array(array_e)
  u = np.array(array_u)
  json_file.close()
  return a, b, c, d, e, u, atmosphere_u

a, b, c, d, e, u, a_u = prepare_vec()
print('ユーザの嗜好: ' + str(a_u))
print('はこだてMOMI-Gフェスタ: ' + str(cos_sim(u, a)))
print('サル山温泉: ' + str(cos_sim(u, b)))
print('五稜星の夢: ' + str(cos_sim(u, c)))
print('市立函館博物館収蔵資料展: ' + str(cos_sim(u, d)))
print('冬の金森神社に願いごと: ' + str(cos_sim(u, e)))