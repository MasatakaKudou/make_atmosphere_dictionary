import csv
import json
import twitterSession

# エンドポイント
SEARCH_TWEETS_URL = 'https://api.twitter.com/1.1/search/tweets.json'
SEARCH_COUNT = 100

def get_tweets(params):
  twitter = twitterSession.get_twitter_session()
  
  req = twitter.get(SEARCH_TWEETS_URL, params = params)
  if req.status_code == 200:
    res = json.loads(req.text)
    f = open('test/test.csv', 'at')
    writer = csv.writer(f)
    for line in res['statuses']:
      keyword = params['q']
      text = (repr(line['text']))
      writer.writerow([keyword, text])
    f.close()
  else:
    print('失敗')

for day in list(range(11, 18)):
  params = {
    'since': f'2021-02-{day}_00:00:00_JST',
    'until': f'2021-02-{day}_23:59:59_JST',
    'exclude': 'retweets',
    'count': SEARCH_COUNT,
    'q': 'テスト'
  }
  get_tweets(params)