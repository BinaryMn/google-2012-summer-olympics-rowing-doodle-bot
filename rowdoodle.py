import time
import win32api, win32con

VK_CODE = {'left_arrow':0x25,
           'right_arrow':0x27}

def press(x):
    win32api.keybd_event(VK_CODE[x], 0,0,0)
    win32api.keybd_event(VK_CODE[x],0 ,win32con.KEYEVENTF_KEYUP ,0)

def play():
	time.sleep(1)
	s = time.time()
	while time.time() - s < 25:
		press("right_arrow")
		time.sleep(0.004)
		press("left_arrow")
		time.sleep(0.004)
		press("right_arrow")
		time.sleep(0.004)
		press("left_arrow")
		time.sleep(0.004)


play()