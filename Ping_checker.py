#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name:       Ping checker
Created by: Christian Morán
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86

##########################################################
"""
import urllib.request
import socket

print("     Ping checker     ")
print("\n")

def check_internet_connection():
   webUrl = urllib.request.urlopen('http://google.com')

   hostname = socket.gethostname()
   IPAddress = socket.gethostbyname(hostname)

   print('IP information')
   print('Computer Name is: ' + hostname)
   print('Computer IP Address: ' + IPAddress)
   print('\n')

   print("Status: " + str(webUrl.status))
   print("Message: " + str(webUrl.msg))
   print("Method: " + str(webUrl._method))
   print("URL: " + webUrl.url)
   print("\n")
   print("Headers: " + str(webUrl.headers))
   print("---------------------------------")

   def look_source_code(webUrl):
      user_response = str(input("Look source code from {}? y/n: ".format(webUrl.url)))
      print('\n')
      if user_response == 'Y' or user_response == 'y':
         print('Source code from {} :'.format(webUrl.url))
         print('\n')
         for lines in webUrl.readlines():
            print(lines)
            print('\n')
      elif user_response == 'N' or user_response == 'n':
         pass
      else:
         return look_source_code(webUrl)

   look_source_code(webUrl)

check_internet_connection()
print("Press Enter/Intro to exit")

input()