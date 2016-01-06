#! python3
#sends the top post from r/Getmotivated to your email
import os
import praw
import smtplib
from email.mime.text import MIMEText
import argparse
import sys


to_email = sys.argv[1]
from_email = sys.argv[2]
password = sys.argv[3]
subreddit = sys.argv[4]

r = praw.Reddit(user_agent='get_motivated')
submissions = r.get_subreddit(subreddit).get_top(limit=1)

for top in submissions:
    top_link = top.url
    title = top.title


top_link += "\n\n Sends the top post of r/Getmotivated."


msg = MIMEText(top_link)
msg['Subject'] = title
msg['From'] = from_email
msg['Reply-to'] = from_email
msg['To'] = to_email



server = smtplib.SMTP('smtp.mail.yahoo.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.close()
