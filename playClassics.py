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
