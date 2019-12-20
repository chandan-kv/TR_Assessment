import pyautogui


class Saplogon(object):
	
	def __init__(self,user,pwd,inst):
		self.userid = user
		self.password = pwd
		self.instance = inst

	def activate_pre_invoke(self):
		pyautogui.hotkey('win', 'd')

	def activate_saplogon(self):
		pyautogui.hotkey('win', 'r')
		pyautogui.typewrite('saplogon')
		pyautogui.press('enter')
		
			


	def activate_post_invoke(self):
		pyautogui.hotkey('win', 'up')

	def activate_Instance(self):
		pyautogui.hotkey('ctrl', 'f')
		pyautogui.typewrite(self.instance)
		pyautogui.press('enter')
			
	def activate_saplogin(self):
		pyautogui.typewrite(self.userid)
		pyautogui.press('tab')
		pyautogui.typewrite(self.password)
		pyautogui.press('enter')


import time

if __name__ == '__main__':
	mysap = Saplogon('XXXXXXXX', 'XXXXXXXXX', 'XXX')
	mysap.activate_pre_invoke()
	time.sleep(2)
	mysap.activate_saplogon()
	time.sleep(7)
	mysap.activate_post_invoke()
	time.sleep(3)
	mysap.activate_Instance()
	time.sleep(5)
	mysap.activate_saplogin()
	time.sleep(3)
	pyautogui.press('enter')
	




