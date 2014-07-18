import sys
import re
from termcolor import colored

# Constants for good and okay speed cut-offs:
GOOD_DL_MIN = 5.0
OKAY_DL_MIN = 1.5

GOOD_UL_MIN = 2.0 
OKAY_UL_MIN = 1.0

if (len(sys.argv)==2):
    fromfile = True
else:
    fromfile = False
if not fromfile:
    print colored("connecting with speedtest server...",attrs=["dark"])
while 1:
    try:
        line = sys.stdin.readline().rstrip()
    except KeyboardInterrupt:
        break

    if not line:
        break

    if(re.search("\[[0-9.]* km\]", line) != None):
    	print colored(line,"cyan")
    	if not fromfile:
            print colored("testing download speed...",attrs=["dark"])
    if(line.find("Cannot") != -1):
    	print line
    	sys.exit(-1)
    if(line.find("Download: ") != -1):
    	#print colored
    	dl = line.split(" ")
    	if(float(dl[1]) > GOOD_DL_MIN):
    		dlcolor = "green"
    	elif(float(dl[1]) > OKAY_DL_MIN):
    		dlcolor = "yellow"
    	else:
    		dlcolor = "red"
    	print colored(dl[0]+" "+dl[1]+" "+dl[2], dlcolor)
    	if not fromfile:
            print colored("testing upload speed...", attrs=["dark"])

    if(line.find("Upload: ") != -1):
    	#print colored
    	ul = line.split(" ")
    	if(float(ul[1]) > GOOD_UL_MIN):
    		ulcolor = "green"
    	elif(float(ul[1]) > OKAY_UL_MIN):
    		ulcolor = "yellow"
    	else:
    		ulcolor = "red"
    	print colored(ul[0]+" "+ul[1]+" "+ul[2], ulcolor)