# -*- coding: utf-8 -*-

import sys,os
from requests_oauthlib import OAuth1Session

path = os.getcwd()+"/"

if __name__ == '__main__':
  
  import bridge,appSettings
  bridge = bridge.bridge()
  getuserInputSearch = bridge.serachUserMessage()
  query,count = getuserInputSearch

  setting = appSettings.setting()
  consumer,cSecret,accessToken,aSecret = setting.k
  url = bridge.getUrl("search")

params = {
         "q": query, 
         "lang":"ja",
         "count" : count
}

twiKey = OAuth1Session(consumer, cSecret, accessToken, aSecret)
request = twiKey.get(url, params = params)

if __name__ == '__main__':
  bridge.searchUserRequest(request)
  getFriendData = bridge.addFriendMethod()
  uId = getFriendData
  url = bridge.getUrl("follow")
  setting = appSettings.setting()

twiKey = OAuth1Session(consumer, cSecret, accessToken, aSecret)
request = twiKey.post("https://api.twitter.com/1.1/friendships/create.json?user_id="+uId+"&follow=true")


if request.status_code == 200 :
   print "フォローしました。"
else :
   print ("Error: %d" % request.status_code)