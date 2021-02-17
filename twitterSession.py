import config
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

# トークン関連
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# セッション確立
def get_twitter_session():
    return OAuth1Session(CK, CS, AT, ATS)