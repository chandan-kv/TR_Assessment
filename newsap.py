import pyautogui


class SapLogon(object):
    
    def __init__(self,user,pwd,inst):
        self.uid = user
        self.pid = pwd
        self.instance = inst
        
    def activate_pre_invoke(self):
        pyautogui.hotkey('win', 'd')
    
    def activate_SapLogon(self):
        try:
            pyautogui.hotkey('win','r')
            pyautogui.typewrite('saplogon')
            pyautogui.press('enter')
            return True
        except:
            return False
        
    def activate_post_invoke(self):
            pyautogui.hotkey('win', 'up')
    
    def open_instance(self):
        try:
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.typewrite(self.instance)
            pyautogui.press('enter')
            return True
        except:
            return False
        
    def SapLogin(self):
        pyautogui.typewrite(self.uid)
        pyautogui.press('tab')
        pyautogui.typewrite(self.pid)
        pyautogui.press('enter')
        
#######################################################
import time
        
if __name__ == '__main__':
    mysap = SapLogon('CKULAGANAVAR', 'Chandu@999', 'DCP')
    mysap.activate_pre_invoke()
    time.sleep(2)
    mysap.activate_SapLogon()
    time.sleep(7)
    mysap.activate_post_invoke()
    time.sleep(2)
    mysap.open_instance()
    time.sleep(5)
    mysap.SapLogin()
    time.sleep(3)
    pyautogui.press('enter')