# -*- coding: utf-8 -*-

class bridge:

#url = "https://api.twitter.com/1.1/users/show.json"
#urlSearchTweet = "https://api.twitter.com/1.1/search/tweets.json"
#urlFriendTwitter = "https://api.twitter.com/1.1/friendships/create.json"
#url = "https://api.twitter.com/1.1/users/suggestions/:slug.json"
#url = "https://api.twitter.com/1.1/statuses/home_timeline.json"


	def serachUserMessage(self) :
		print "検索するワードを入れてください。"
		self.query = raw_input()
		print self.query+"で検索します。何件検索しますか？"
		self.count = raw_input()
		return [self.query,self.count]		
