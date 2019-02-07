#!/usr/bin/python3
#only work in linux
#usage: ./email-generator.py | ./email-filter.py
#dont forget to chmod so the code can be run
#not work in code playground
import sys
import re
#for line in sys.stdin:
# sys.stdout.write(line)

def email_filter(email, official=1):
 smtp = ["gmail", "yahoo", "hotmail", "protonmail", "kevin"]
 
 if official:
  ya = False
  for i in smtp:
   if re.match(r"([\w._]+)@{smtp}([\.])com".format(smtp=i), email):
    ya = True
  return ya
  
 if re.match(r"([\w._]+)@([\w]+)([\.])([\w]+)", email):
  return True
 return False
   
if __name__ == "__main__":
 for line in sys.stdin:
  if (email_filter(line)):
   print(line, end="\r")
