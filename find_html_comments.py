#!/usr/bin/env python3

import requests
import re

file = '/root/HTB/solid_state/gobust'
string =re.compile("((.*\n){2})\<\!((.*\n){2})")
#string = "\<\!"
with open(file) as f:
	lines = f.readlines()
	for x in lines:
		line = x.split(' ')[0]
		print ("checking page "+line+"\n")
		req = requests.get(line)
		if req.status_code == 200:
			for i in req.iter_lines():
				if "<!" in str(i):
					print (str(i))
		else:
			print ("can't reach "+line+"\n")

f.close()
