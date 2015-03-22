import virtkey
import time
from Xlib import X, display
#from pymouse import PyMouse

acceptableInputs="Aa Bb 	Cc 	Dd 	Ee 	Ff 	Gg 	Hh 	Ii 	Jj 	Kk 	Ll 	Mm 	Nn 	Oo 	Pp 	Qq 	Rr 	Ss 	Tt 	Uu 	Vv 	Ww 	Xx 	Yy 	Zz .,!"

aCmnds=["Ee Nn "] #13+7
bCmnds=["Rr Dd"] # 10
leCmnds=["Tt Ff Uu Xx Yy ; Zz"] # 9 +2 + 3
riCmnds=["Aa Kk Pp Qq .,!  Vv"] # 9 +2 +3
upCmnds=["Oo Bb Hh"] # 9 +6 
dnCmnds=["Ii Gg Ss"] # 9 +6 
lCmnds=["Ww "] # 2.3 
rCmnds=["Mm "] # 2.4
seCmnds=["Cc Jj"] # 2.7
stCmnds=["Ll "] # 4


v = virtkey.virtkey()

def pressA():
	v.press_unicode(ord("a"))
	v.release_unicode(ord("a"))

def pressB():
	v.press_unicode(ord("b"))
	v.release_unicode(ord("b"))

def pressUp():
	v.press_unicode(ord("u"))
	v.release_unicode(ord("u"))

def pressDown():
	v.press_unicode(ord("d"))
	v.release_unicode(ord("d"))

def pressLeft():
	v.press_unicode(ord("l"))
	v.release_unicode(ord("l"))

def pressRight():
	v.press_unicode(ord("r"))
	v.release_unicode(ord("r"))

def pressLbtn():
	v.press_unicode(ord("y"))
	v.release_unicode(ord("y"))

def pressRbtn():
	v.press_unicode(ord("i"))
	v.release_unicode(ord("i"))

def pressSelect():
	v.press_unicode(ord("e"))
	v.release_unicode(ord("e"))

def pressStart():
	v.press_unicode(ord("w"))
	v.release_unicode(ord("w"))

def pressSpace():
	v.press_unicode(ord("s"))
	v.release_unicode(ord("s"))

mob=open("mobydick.txt", "r")
bib=open("bible.txt", "r")
nin=open("1984.txt","r")
oed=open("dictionary.txt","r")
test=open("test.txt","r")

runcount = 0

def loadDataFromFile(filename):
    inFile = open (filename, 'r')
    list = []
    for line in inFile:
        val = str(line)
        list.append(val)
    inFile.close()
    return (list)

mobyPost=[]
biblPost=[]
I984Post=[]
dictPost=[]

def procMoby():
	for line in mob:
		for c in line: 
			if c != '\n' and c != '\r':
				mobyPost.append(c)
def procBible():
	for line in bib:
		for c in line: 
			if c != '\n' and c != '\r':
				biblPost.append(c)
def proc1984():
	for line in nin:
		for c in line: 
			if c != '\n' and c != '\r':
				I984Post.append(c)
def procDict():
	for line in oed:
		for c in line: 
			if c != '\n' and c != '\r':
				dictPost.append(c)


def procBooks():
	proc1984();
	procDict();
	procMoby();
	procBible();


def main():
	count = 0;
	while True:
		target = 1
		procChar(mobyPost[count % len(mobyPost)], target)
		target = 2
		procChar(biblPost[count % len(biblPost)], target)
		target = 3
		procChar(I984Post[count % len(I984Post)], target)
		target = 4
		procChar(dictPost[count % len(dictPost)], target)

		count = count + 1
		if(count % 100 == 0):
			time.sleep(1.5)


def procChar(cmnd, target):
	if cmnd in acceptableInputs:
		click(target)
		print str(target) + cmnd

		if cmnd in aCmnds:
			pressA()
		if cmnd in bCmnds:
			pressB()
		if cmnd in upCmnds:
			pressUp()
		if cmnd in dnCmnds:
			pressDown()
		if cmnd in leCmnds:
			pressLeft()
		if cmnd in riCmnds:
			pressRight()
		if cmnd in lCmnds:
			pressLbtn()
		if cmnd in rCmnds:
			pressRbtn()
		if cmnd in seCmnds:
			pressSelect()
		if cmnd in stCmnds:
			pressStart()

def click(target):

	d = display.Display()
	s = d.screen()
	root = s.root
	root.warp_pointer(300,300)
	d.sync()

	if target == 1:
		d = display.Display()
		s = d.screen()
		root = s.root
		root.warp_pointer(300,300)
		d.sync()
	elif target == 2:
		d = display.Display()
		s = d.screen()
		root = s.root
		root.warp_pointer(300,600)
		d.sync()
	elif target == 3:
		d = display.Display()
		s = d.screen()
		root = s.root
		root.warp_pointer(600,300)
		d.sync()
	else: 
		d = display.Display()
		s = d.screen()
		root = s.root
		root.warp_pointer(600,600)
		d.sync()

#Moby Dick, Upper Left
def sendUL():
	print "t"
#1984, Upper Right
def sendUR():
	print "test"

#The Bible, Bottom Left
def sendBL():
	print "test"

#Dictionary: Bottom Right
def sendBR():
	print "test"

procBooks()
main()