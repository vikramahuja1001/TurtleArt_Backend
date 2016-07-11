import os
import re
import time
import ast
import json


import subprocess
from backend import *


b=backend()

def init(button):
	print "Initializing the repo"
	#b = backend()
	b.local_init("turtle", "TurtleJS")
	print b.repo_name
	a = "turtle_vikram.tb"
	b.set_current_file_name(a)
	c = "[[0,[\"start\",{\"collapsed\":false,\"xcor\":0,\"ycor\":0,\"heading\":0,\"color\":0,\"shade\":50,\"pensize\":5,\"grey\":100}],250,150,[null,null,null]]]"
	b.create_file(a,c)
	b.set_current_file_name(a)
	print "File Created"


def add(button):
	#b.load_repo("turtle")
	print "Adding"
	b.add(b.current_file_name)
	print "File Added: i", 
	print b.current_file_name

def status(button):
	print "Checking status"
	#b.load_repo("turtle")
	print b.current_file_name
	print str(b.get_status())


def commit(button):
	print "Commiting"
	#b.load_repo("turtle")
	a = "First Commit"
	b.commit(a)
	print "commited"

def commithistory():
	#b.load_repo("turtle")
	print b.current_file_name
	a = b.get_commit_history(b.current_file_name)
	c = ""
	for i in a:
		c += str(i)
	print c 
	print type(a)
	print len(a)
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	c = "<h2>" + c + "</h2>"
	return img+c


def revertcommit():
	#b.load_repo("turtle")
	print b.current_file_name
	#a = b.get_commit_history(b.current_file_name)
	a = b.get_commit_id_and_message(b.current_file_name)
	c = ""
	count = 1
	for i in a:
		count +=1
		c += "<a onclick=\"_returncommit(" + str(count/2) + ")\" href=\"javascript:void(0)\">" + str(i) + "</a>"
	print c 
	print type(a)
	print len(a)
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	c = "<h2>" + c + "</h2>"
	return img+c


def returncommit():
	print "vikram"
	print b.current_file_name
	print b.repo_name
	print b.repo_path
	print os.getcwd()
	os.system('ls')
	diff_filename = "diff_file_%s" % (b.current_file_name)
	cmdstring = "python app/diff_func.py %s > diffs/%s" % (b.current_file_name, diff_filename)
	os.system(cmdstring)
	file_object = open("diffs/%s" % (diff_filename), "r")
	a = file_object.readlines()
	c = []
	for i in a:
		if len(i)> 200:
			c.append(i)

	d = []
	d.append(c[0])
	tot = len(c) - 2
	if tot > 0:
		i = 1
		while i<=tot:
			d.append(c[i])
			i +=2
	d.append(c[tot+1])
	for i in range(len(d)):
		d[i] = d[i][1:]
		print i

	a = str(d[int(data) - 1] )
	print a
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	return a




def difftree():
	#b.load_repo("turtle")
	#a = b.get_diff()
	#print a
	print b.current_file_name
	print b.repo_name
	print b.repo_path
	print os.getcwd()
	os.system('ls')
	diff_filename = "diff_file_%s" % (b.current_file_name)
	cmdstring = "python app/diff_func.py %s > diffs/%s" % (b.current_file_name, diff_filename)
	os.system(cmdstring)
	file_object = open("diffs/%s" % (diff_filename), "r")
	a = file_object.readlines()
	c = []
	for i in a:
		if len(i)> 200:
			c.append(i)

	for i in c:
		print i
	print "Vikram"
	print len(c)
	print type(c)

	i = 0
	while i < len(c):
		len1 = len(c[i])
		len2 = len(c[i+1])
		print len1
		print len2
		c[i] = c[i][1:]
		print c[i]

		c[i+1] = c[i+1][1:]
		print c[i+1]
		print type(c[i])

		blocks1 = {}
		blocks2 = {}
		rep1 = ""
		rep2 = ""
		for j in c[i]:
			if j == ".":
				rep1 += "0"
			else:
				rep1 += j

		for j in c[i+1]:
			if j == ".":
				rep2 += "0"
			else:
				rep2 += j

		print rep1
		print rep2
		rep1 = json.loads(rep1)
		rep2 = json.loads(rep2)
		for j in rep1:
			print j
		for j in rep2:
			print j
		for j in rep1:
			print len(j)
		i = i+2

	#print output
	#print b.get_diff()
	#print type(a)
	a = "Hello"
	return a


def loadrepo():
	b.load_repo("turtle")
	b.set_current_file_name("turtle_vikram.tb")
	print b.current_file_name
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	a = "<h2>Repo loaded: " + b.repo_name + "</h2>"
	return img+a

def save(button):
	a = request.form['data']
	print a
	print type(a)
	a = str(a)
	b.edit_file(b.current_file_name,a)
	print b.current_file_name
	a = "<h2> File Saved: " + b.current_file_name + "</h2>" 
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	return img+a
