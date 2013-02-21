#!/usr/bin/python

import sys, os
from subprocess import Popen, PIPE

path1 = sys.argv[1]
path2 = sys.argv[2]

recurse = True
hashcount = 0
differcount = 0

def listdir(path1, path2):
	global recurse, hashcount, differcount
	for entry in sorted(os.listdir(os.path.join(path1,".md5"))):
		localhashfile = os.path.join(path1,".md5",entry)
		remotehashfile = os.path.join(path2,".md5",entry)
		if not os.path.exists(remotehashfile):
			print "remote has no hash for "+os.path.join(path1,entry)
		else:
			localhash = open(localhashfile).read().strip()
			remotehash = open(remotehashfile).read().strip()
			if localhash != remotehash:
				print "hash differs: "+os.path.join(path1,entry)
				differcount += 1
		hashcount += 1				

#		elif os.path.isdir(entry):
#			if recurse:
#				...

listdir(path1, path2)

print str(hashcount)+" hashes compared. "+str(differcount)+" differ."
