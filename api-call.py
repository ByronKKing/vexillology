import praw
import urllib.request as urlreq
import os
import pandas as pd

###scrape images from imgur
###write program to produce random flag, or string search dataset and display flag based on user-request

flair = ['Collection','Historical','Current','Redesigns','OC','Fictional']

oldFlags = pd.read_csv("flags.csv")

red = praw.Reddit("vexill-scrape")

vexill = red.subreddit("Vexillology")

dictList = []
for submission in vexill.top(time_filter='day',limit=25):
	print("Title: ", submission.title)
	print("-----\n")
	if submission.link_flair_text in flair and submission.id not in oldFlags.id:
		currentDict = {}
		currentDict['id'] = submission.id
		currentDict['title'] = submission.title
		currentDict['score'] = submission.score
		currentDict['url'] = submission.url
		currentDict['created'] = submission.created
		currentDict['created_utc'] = submission.created_utc
		currentDict['author'] = submission.author
		currentDict['author_flair'] = submission.author_flair_text
		currentDict['link_flair'] = submission.link_flair_text
		if submission.url[-3:] in ['jpg','png']:
			currentDict['image'] = os.getcwd()+"/vexill-flags/"+submission.id+"."+submission.url[-3:]
			urlreq.urlretrieve(submission.url, os.getcwd()+"/vexill-flags/"+submission.id+"."+submission.url[-3:])
		else:
			currentDict['image'] = None
		dictList.append(currentDict)

newFlags = pd.DataFrame(dictList)

oldFlags = oldFlags.append(newFlags)

oldFlags.to_csv("flags.csv",index=False)




