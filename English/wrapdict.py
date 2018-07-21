#!/usr/bin/python

import sys

headerstring="<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\"></head><body bgcolor=\"#ffffff\">"
commentstring="<!-- This file was created from ISLEdict.txt using wrapdict.py. --><!-- Do not edit this file directly: edit ISLEdict.txt instead -->"
prestring="<pre>"
footerstring="</pre></body></html>"

with open('ProjectPage.html') as f:
    info_string = f.read()
    
if len(sys.argv) < 3:
    sys.stderr.write("USAGE: wrapdict.py dict.txt dict.html")
    sys.exit(0)
    
with open(sys.argv[2],'w') as outputfile:
    outputfile.write(headerstring+commentstring+"\n")
    outputfile.write(info_string)
    outputfile.write(prestring+"\n")
    with open(sys.argv[1]) as inputfile:
        for line in inputfile:
            outputfile.write(line)
    outputfile.write(footerstring+"\n")


