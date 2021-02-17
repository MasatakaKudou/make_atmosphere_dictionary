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
    f = open('miharashikouen/miharashikouen.csv', 'at')
    writer = csv.writer(f)
    for line in res['statuses']:
      keyword = params['q']
      text = (repr(line['text']))
      writer.writerow([keyword, text])
    f.close()
  else:
    print('失敗')

params = {
  'since': '2021-02-10_00:00:00_JST',
  'until': '2021-02-10_23:59:59_JST',
  'exclude': 'retweets',
  'count': SEARCH_COUNT,
  'q': '見晴公園'
}
get_tweets(params)