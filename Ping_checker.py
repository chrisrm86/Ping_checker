#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name: 		Ping checker
Created by: Christian Morán
e-mail: 	christianrmoran86@gmail.com
More code: 	http://github.com/chrisrm86

##########################################################
"""
import urllib.request


print("     Ping checker     ")
print("\n")

def check_internet_connection():
   webUrl = urllib.request.urlopen('http://google.com')

   print("Status: " + str(webUrl.status))
   print("Message: " + str(webUrl.msg))
   print("Method: " + str(webUrl._method))
   print("URL: " + webUrl.url)
   print("\n")
   print("Headers: " + str(webUrl.headers))
   print("---------------------------------")
   print("Source code from " + webUrl.url)
   print("\n")

   for lines in webUrl.readlines():
       print(lines)
       print('\n')

check_internet_connection()

print("Press Enter/Intro to exit")
input()
