import csv
import os
import json
import twitterSession

class GetTweets:
  def make_dir(self, EN_NOUN):
    os.mkdir(EN_NOUN)

  def get_tweets(self, params, EN_NOUN):
    # エンドポイント
    SEARCH_TWEETS_URL = 'https://api.twitter.com/1.1/search/tweets.json'
    twitter = twitterSession.get_twitter_session()
    
    req = twitter.get(SEARCH_TWEETS_URL, params = params)
    if req.status_code == 200:
      res = json.loads(req.text)
      f = open(f'{EN_NOUN}/{EN_NOUN}.csv', 'at')
      writer = csv.writer(f)
      for line in res['statuses']:
        keyword = params['q']
        text = (repr(line['text']))
        writer.writerow([keyword, text])
      f.close()
    else:
      print('失敗')