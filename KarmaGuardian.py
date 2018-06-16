import praw 
import config 
import time 

def login():
    print("Logging in as: " + config.username)
    reddit = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent)
    print("Logged in!")
    return reddit

def guard_karma(reddit):
    user = reddit.user.me()
    for comment in user.comments.controversial(limit=100):
        if comment.score < config.threshold:
            print("Deleted comment: " + comment.id)
            comment.delete()

print("KarmaGuardian by ShantnuS")
reddit = login()
running = True

while running:
    guard_karma(reddit)
    time.sleep(60)