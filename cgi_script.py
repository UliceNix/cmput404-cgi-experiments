#!/usr/bin/env python

import cgi
import json
import os
import sys

form = cgi.FieldStorage()
user = form.getvalue("user") if form.getvalue("user") else ""
password = form.getvalue("password") if form.getvalue("password") else ""
loggedinok = False
if user == "bob" and password == "test123":
	loggedinok = True
if 'loggedin=true' in os.environ["HTTP_COOKIE"]:
	loggedinok = True

# stdout is connected to cgi_server
print "Content-type: text/html"
if loggedinok:
	print "Set-Cookie: loggedin=true"
print 
print "<HTML><BODY><h1> Hello, tester! </h1>"

print "<FORM method='POST'>Username: <input name='user'/><br/><br/>Password:<input name='password' type='password'/><br/>"
print "<button type='submit'>Log In</button>"
print "</FORM>"

print ("<h5> The query string: " + os.environ["QUERY_STRING"] + "</h5>")
print ("<h5> The browser     : " + os.environ["HTTP_USER_AGENT"] + "</h5>")

print "<p>"
print "User name was: " + user + "."
print "Password was: " + password + "."
print "Loged In Ok" if loggedinok else ""
print "</p>"
cgi.print_environ()

print json.dumps(dict(os.environ), indent=4)

print "</BODY></HTML>"
