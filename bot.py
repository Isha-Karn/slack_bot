from python_imagesearch.imagesearch import *
import pyautogui
import time

def iclick(img):
	pos = imagesearch("./" + img)
	if pos[0] != -1: #Image navetida -1 auxa
		print("position : ", pos[0], pos[1])
		pyautogui.click(pos[0]+ 10, pos[1] + 10)
		pyautogui.click(pos[0]+ 10, pos[1] + 10)
		return 1
	else:
		return 0

slackOpen= False
gogetters= False
while 1:
	time.sleep(5)
	if slackOpen == False:
		if iclick("slack.png")==1:
			slackOpen= True
	
	if gogetters == False:
		if iclick("gogetters.png")==1:
			gogetters= True
			time.sleep(5)
			pyautogui.write('Good Morning Team') 
			pyautogui.press('enter')
			break








		

	
