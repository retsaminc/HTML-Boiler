#!/usr/bin/python -tt

import os
import sys
import urllib2


def create(dir):
	if not os.path.exists(dir):
    		os.makedirs(dir)

def install(dir,file):
	output = open(dir,'wb')
	if(file):
		output.write(file.read())
	else:
		output.write('')
	output.close()


path = sys.path[0] #grabs current path this file is executed
#path="C:\Users/retsam\Desktop\gpe\py_web_structure"  #alternatively you can insert the path to the directory of interest here
dirList=os.listdir(path)

print dirList

create(path+"/style")
create(path+"/js")

index = urllib2.urlopen("https://raw.github.com/retsaminc/HTML-Boiler/master/index.html")
jquery = urllib2.urlopen("http://code.jquery.com/jquery-1.7.2.min.js")
ninesixty = urllib2.urlopen("https://raw.github.com/nathansmith/960-Grid-System/master/code/css/960.css")
modernizer = urllib2.urlopen("http://modernizr.com/downloads/modernizr-2.5.3.js")
#install(filepath+filename,file || [])
install('js/jquery.js', jquery)
install('js/modernizer.js', modernizer)
install('style/960.css', ninesixty)
install('js/main.js',[]) 
install('style/style.css',[])
install('index.html',index)