import csv

# csvファイルを開く
csv_file = open('lucky.csv', 'r')
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

unique_tweet_list = list(map(list, set(map(tuple, tweet_list))))

new = open('lucky_1.csv', 'w')
writer = csv.writer(new)
for unique_tweet in unique_tweet_list:
    keyword = unique_tweet[0]
    text = unique_tweet[1]
    writer.writerow([str(keyword), str(text)])
new.close()