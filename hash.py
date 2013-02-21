#!/usr/bin/python

import sys, os
from subprocess import Popen, PIPE

filename = None
if len(sys.argv) > 1:
	filename = sys.argv[1]

recurse = True
hashcount = 0
differcount = 0

if not os.path.exists(".md5"):
	os.mkdir(".md5")

def md5(fname):
	out = Popen(["md5sum", fname], stdout=PIPE).communicate()[0]
	return out[:32]

def hash(fname):
	global hashcount, differcount
	md5hash = md5(fname)
	hashcount += 1
	hashfile = ".md5/"+os.path.basename(fname)
	oldhash = ""
	if os.path.exists(hashfile):
		oldhash = open(hashfile).read().strip()
	if md5hash != oldhash:
		print md5hash+"  "+fname
		open(hashfile, "w").write(md5hash)
		differcount += 1

def listdir(path):
	global recurse
	for entry in sorted(os.listdir(path)):
		if os.path.isfile(entry):
			hash(os.path.join(path, entry))
#		elif os.path.isdir(entry):
#			if recurse:
#				listdir(os.path.join(path,entry))

if filename is None:
	listdir(".")
else:
	hash(filename)

print str(hashcount)+" files hashed. "+str(differcount)+" modifications."
