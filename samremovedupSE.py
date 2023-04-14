#!/usr/bin/env python
#pontus.skoglund@gmail.com

import sys

remove=True

lastRead = None
for line in sys.stdin:
	if line[0] == '@':
		print line.rstrip('\n')
		continue
		
	fields = line.split()
	flag = int(fields[1])
	if flag & 0x4: #unmapped read
		continue
    
	chrname = fields[2]
	pos = int(fields[3])
	seq = fields[9]
	
	if lastRead == (chrname, pos):  #True if read is a duplicate
			continue
	else: #new start position, use this read
		lastRead = (chrname, pos)
		print line.rstrip('\n')