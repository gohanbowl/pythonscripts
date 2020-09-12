#!/usr/bin/env python3

import requests


file = '<path_to_file>'
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
