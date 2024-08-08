#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginposts = 0 # counter for successful POSTS

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    for lines in kfile:
        #If the post appears in the line
        if "POST" in lines:
           loginposts += 1

print(f"There were {loginposts} successful POSTs")  # prints the # of successful POSTS
