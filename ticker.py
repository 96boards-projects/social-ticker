#################################################################
# Title: ticker.py
# Author: Sahaj Sarup
# Copyright (c) 2018 Linaro Limited
#################################################################

import tweepy
import requests
import time
import serial

ser = serial.Serial("/dev/tty96B0",9600)
ser.flushInput()

ytapikey = ' '
ytid = ' '

twuname = ' '
twconsumer_key = ' '
twconsumer_secret = ' '
twaccess_token = ' '
twaccess_token_secret = ' '

instaid = ' '

instaurl = 'https://instagram.com/web/search/topsearch/?query={' + instaid  + '}'
yturl = 'https://www.googleapis.com/youtube/v3/channels?id=' + ytid  + '&key=' + ytapikey  + '&part=statistics&fields=items(statistics(subscriberCount))'

auth = tweepy.OAuthHandler(twconsumer_key,twconsumer_secret)
auth.set_access_token(twaccess_token,twaccess_token_secret)
api = tweepy.API(auth)


def update():
	global instadat, ytjson, user
	instadat = requests.get(instaurl).json()
	ytjson = requests.get(yturl).json()
	user = api.get_user(twuname)

def tw():
	i = 0
	count = float(user.followers_count)
	if count < 1000:
		out = '1s' + "{:4.0f}".format(count) + ' ' + 't'
	elif count > 999 and count < 1000000:
		out = '1s' + "{:4.0f}".format(count/1000) + 'K' + 't'
	elif count > 999999 and count < 1000000000:
		out = '1s' + "{:4.0f}".format(count/1000000) + 'M' + 't'
	elif count > 999999999:
		out = '1s' + "{:4.0f}".format(count/1000000000) + 'B' + 't'
	print out
	ser.write(out)

def insta():
	count = float(instadat['users'][0]['user']['follower_count'])
        if count < 1000:
                out = '3s' + "{:4.0f}".format(count) + 't'
        elif count > 999 and count < 1000000:
                out = '3s' + "{:4.0f}".format(count/1000) + 'K' + 't'
        elif count > 999999 and count < 1000000000:
                out = '3s' + "{:4.0f}".format(count/1000000) + 'M' + 't'
        elif count > 999999999:
                out = '3s' + "{:4.0f}".format(count/1000000000) + 'B' + 't'

	print out
	ser.write(out)


def yt():
	count = float(ytjson['items'][0]['statistics']['subscriberCount'])

        if count < 1000:
                out = '2s' + "{:4.0f}".format(count) + 't'
        elif count > 999 and count < 1000000:
                out = '2s' + "{:4.0f}".format(count/1000) + 'K' + 't'
        elif count > 999999 and count < 1000000000:
                out = '2s' + "{:4.0f}".format(count/1000000) + 'M' + 't'
        elif count > 999999999:
                out = '2s' + "{:4.0f}".format(count/1000000000) + 'B' + 't'


	print out
	ser.write(out)


if __name__ == '__main__':
  time.sleep(15)
  while True:
  	update()
  	tw()
  	time.sleep(10)
	insta()
	time.sleep(10)
  	yt()
	time.sleep(10)

