import praw

red = praw.Reddit("vexill-scrape")

vexill = red.subreddit("Vexillology")

for submission in vexill.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
