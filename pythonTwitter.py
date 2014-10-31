# -*- coding: utf-8 -*-

import sys,codecs,json,os
from requests_oauthlib import OAuth1Session

sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='ignore')
reload(sys)
sys.setdefaultencoding('utf-8')
   
path = os.getcwd()+"/"

if __name__ == '__main__':
  
  import bridge,appSettings
  bridge = bridge.bridge()
  getuserInputSearch = bridge.serachUserMessage()
  query,count = getuserInputSearch

  setting = appSettings.setting()
  consumer,cSecret,accessToken,aSecret = setting.k


sys.exit()

params = {
         "q": query, 
         "lang":"ja",
         "count" : count
}

twiKey = OAuth1Session(consumer, cSecret, accessToken, aSecret)
request = twiKey.get(url, params = params)

if request.status_code == 200:
    timeline = json.loads(request.text,'utf-8')
    for tweet in timeline["statuses"]:
        if tweet["user"]["friends_count"] > tweet["user"]["followers_count"] :
          print("--------------------------")
          print(tweet["id"])
          print(tweet["user"]["name"])
          print(tweet["user"]["friends_count"])
          print(tweet["user"]["followers_count"])
          print("--------------------------")
          print(tweet["user"]["description"])
          print("--------------------------")
else :
    print ("Error: %d" % request.status_code)


sys.exit()



print "ＩＤを入力？"
uId = raw_input()
print "名前を入力?"
nameId = raw_input()

if len(uId) == 0 :
  uId = "true"
elif len(nameId) == 0 :
  nameId = "true" 

params = {
    "user_id ": uId,
    "screen_name ": nameId,
    "follow" : "false"
}

request = twiKey.post(url, params = params)

if request.status_code == 200 :
   print "フォローしました。"
else :
   print ("Error: %d" % request.status_code)