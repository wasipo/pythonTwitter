# -*- coding: utf-8 -*-

class bridge:

	def serachUserMessage(self) :
		print "検索するワードを入れてください。"
		self.query = raw_input()
		print self.query+"で検索します。何件検索しますか？"
		self.count = raw_input()
		return [self.query,self.count]		

	def addFriendMethod(self) :
		print "ＩＤを入力？"
		self.uId = raw_input()
		return self.uId

	def getUrl(self,prt) :
		if prt == "search" :
			return "https://api.twitter.com/1.1/search/tweets.json"
		elif prt == "follow" :
			return "https://api.twitter.com/1.1/friendships/create.json"
		elif prt == "postTweet" :
			return "https://api.twitter.com/1.1/statuses/update.json"

	def searchUserRequest(self,reqObj) :
		import json

		if reqObj.status_code == 200:
		    timeline = json.loads(reqObj.text,'utf-8')
		    for tweet in timeline["statuses"]:
		        if tweet["user"]["friends_count"] > tweet["user"]["followers_count"] :
		          print("--------------------------")
		          print(tweet["user"]["id"])
		          print(tweet["user"]["name"])
		          print(tweet["user"]["friends_count"])
		          print(tweet["user"]["followers_count"])
		          print("--------------------------")
		          print(tweet["user"]["description"])
		          print("--------------------------")
		else :
		    print ("Error: %d" % reqObj.status_code)