#!/usr/bin/env python3
from datetime import datetime
SCRIPT_NOW = datetime.now()
from datetime import timedelta
import feedparser
import requests

WEBHOOK_URLS = [
        'webhook url. replace these',
        'another one',
        'you can just have one item in this list to use only one'
]
def sendWebhookMessage(msg) :
    for url in WEBHOOK_URLS:
        requests.post(url, data={
            "content": msg
        })
    return

#sendWebhookMessage('Testing! Post authorized by an administator ! Ignore this!')

DATE_OFFSET = timedelta(days=1443,hours=28)
TIME_AGO_MAX = timedelta(hours=1)
ZERO_OFFSET = timedelta(seconds=0)
FEED = feedparser.parse('teo.xml')

msg = '**THIS HOUR\'S ANTIQUE TEO POSTS:**'
foundSomePosts = False
for entry in FEED.entries:
    postTime = datetime.strptime(entry.published,'%a, %d %b %Y %H:%M:%S +0000')
    delayTime = postTime + DATE_OFFSET
    timeAgo = SCRIPT_NOW - delayTime
    if timeAgo <= TIME_AGO_MAX and timeAgo >= ZERO_OFFSET:
        foundSomePosts = True
        msg = msg + '\nORIGINAL POST TIME: ' + str(postTime) + ' UTC | DELAYED TIME: ' + str(timeAgo) + ' AGO | LINK: '  + entry.link

if foundSomePosts:
    print('Found Posts! Posting Posts!!')
    sendWebhookMessage(msg)
else:
    print('No Post!')
