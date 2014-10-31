# -*- coding: utf-8 -*-

class bridge:


	def serachUserMessage(self) :
		print "検索するワードを入れてください。"
		self.query = raw_input()
		print self.query+"で検索します。何件検索しますか？"
		self.count = raw_input()
		return [self.query,self.count]		
