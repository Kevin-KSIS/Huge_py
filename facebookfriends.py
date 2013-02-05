#!/usr/bin/env python
import re
from mechanize import Browser
from mechanize import _http
from BeautifulSoup import BeautifulSoup
import cookielib
import json

#### Start Config ##################
browser_client = Browser()
web_locations = "http://facebook.com/" #Main Web Url
login_page = "login.php"  #Path to login page in main web
user_page = "home.php"   #Path to home page in main web
cj = cookielib.LWPCookieJar()
browser_client.set_cookiejar(cj)
browser_client.set_handle_equiv(True)
browser_client.set_handle_redirect(True)
browser_client.set_handle_referer(True)
browser_client.set_handle_robots(False)
browser_client.set_handle_refresh(_http.HTTPRefreshProcessor(), max_time=1)
browser_client.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.6) Gecko/20100720 Gentoo Firefox/3.6.6')]
#### End Config ####################

def facebook_login(input_username , input_password):
    user = input_username
    password = input_password
    page = web_locations+login_page
    browser_client.open(page)
    browser_client.select_form(nr=0)
    browser_client["email"]=user
    browser_client["pass"]=password
    browser_client.submit()
    next_page = web_locations+user_page
    browser_client.open(next_page)


def my_frends():
    sk_friends_page = "friends/edit/?sk=all"
    myid=str(000000000) # my fb id number
    ajax_friends = "ajax/typeahead_friends.php?u="+myid+"&__a=1"
    next_page = web_locations+ajax_friends
    browser_client.open(next_page)
    js=browser_client.response().read()
    result = js.strip('for\ (;;);')
    friends = json.loads(result)

    for friend in friends['payload']['friends']:
        print repr(friend['t'])

facebook_login("user@server.com", "yourpassword")
my_frends()
