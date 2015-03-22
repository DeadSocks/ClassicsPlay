import virtkey
import time
#from pymouse import PyMouse

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
	while true:


		count = count + 1


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