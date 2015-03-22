import win32api, win32con
import time
import random
import sys
import msvcrt 
#def buttonL():
#def buttonR():
t = 0
pressTime = 0.005
moveTime = 0.005
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def leftArrow():#A
    win32api.keybd_event(0x41,0,0,0)
    time.sleep(moveTime)
    win32api.keybd_event(0x41,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(t)
def rightArrow():#D
    win32api.keybd_event(0x44,0,0,0)
    time.sleep(moveTime)
    win32api.keybd_event(0x44,0,2,0)
    time.sleep(t)
def upArrow():#W
    win32api.keybd_event(0x57,0,0,0)
    time.sleep(moveTime)
    win32api.keybd_event(0x57,0,2,0)
    time.sleep(t)
def downArrow():#S
    win32api.keybd_event(0x53,0,0,0)
    time.sleep(moveTime)
    win32api.keybd_event(0x53,0,2,0)
    time.sleep(t)
def buttonA():#Z key
    win32api.keybd_event(0x5A,0,0,0)
    time.sleep(pressTime)
    win32api.keybd_event(0x5A,0,2,0)
    time.sleep(t)
def buttonB():#X key
    win32api.keybd_event(0x58,0,0,0)
    time.sleep(pressTime)
    win32api.keybd_event(0x58,0,2,0)
    time.sleep(t)
def Start():#ENTER key
    win32api.keybd_event(0x0D,0,0,0)
    time.sleep(pressTime)
    win32api.keybd_event(0x0D,0,2,0)
    time.sleep(t)
def Select():#BACKSPACE key
    win32api.keybd_event(0x08,0,0,0)
    time.sleep(pressTime)
    win32api.keybd_event(0x08,0,2,0)
    time.sleep(t)
def testFunc():#GO LEFT
        time.sleep(1.5)
        """win32api.keybd_event(0x25,0,2,0)#win32con.KEYEVENTF_EXTENDEDKEY
        time.sleep(2)
        win32api.keybd_event(0x25,0,0,0)#win32con.KEYEVENTF_KEYUP
        time.sleep(.1)"""
        #TypeKey(0x58,2)
        downArrow()
        

def PressKey(down, key):
  """Presses or unpresses a key.

  Uses keybd_event to simulate either depressing or releasing
  a key

  Args:
    down: Whether the key is to be pressed or released
    key:  Virtual key code of key to press or release
  """

  # keybd_event injects key events at a very low level (it's the
  # Windows API keyboard device drivers call) so this is a very
  # reliable way of simulating user input
  win32api.keybd_event(key, 0, (not down) * win32con.KEYEVENTF_KEYUP)

def TypeKey(key, keystroke_time):
  """Simulate a keypress of a virtual key.

  Args:
    key: which key to press
    keystroke_time: length of time (in seconds) to "hold down" the key
                    Note that zero works just fine

  Returns:
    None
  """
  # This just wraps a pair of PressKey calls with an intervening delay
  PressKey(True, key)
  time.sleep(keystroke_time)
  PressKey(False, key)
  
up =	740206
left=	740206
right	=740206
down	=740206
b	=553387
a	=553387
start	=325360
select	=47308

def playGame():
    up =	740206
    left=	643346
    right	=611908
    down	=599127
    b	=553387
    a	=1044869
    start	=125360
    select	=47308
    y = 1
    time.sleep(2)
    #click(300,300)
    while(win32api.GetKeyState(0x1B) > -100):#3000 runs per minute
        x = random.randint(0, up+left+right+down+b+a+start+select)
        if 0 < x < up:
            upArrow()
            upArrow()
            upArrow()
            upArrow()
            upArrow()
            print 'UP'
        elif up <= x < up+left:
            leftArrow()
            leftArrow()
            leftArrow()
            leftArrow()
            leftArrow()
            print 'LEFT'
        elif up+left <= x < up+left+right:
            rightArrow()
            rightArrow()
            rightArrow()
            rightArrow()
            rightArrow()
            print 'RIGHT'
        elif up+left+right <= x < up+left+right+down:
            downArrow()
            downArrow()
            downArrow()
            downArrow()
            downArrow()
            print 'DOWN'
        elif up+left+right+down <= x < up+left+right+down+b:
            buttonB()
            print "B"
        elif up+left+right+down+b <= x < up+left+right+down+b+a:
            buttonA()
            print 'A'
        elif up+left+right+down+b+a <= x < up+left+right+down+b+a+start:
            Start()
            print 'START'
        elif up+left+right+down+b+a+start <= x < up+left+right+down+b+a+start+select:
            Select()
            print 'SELECT'
    sys.exit("Error message")