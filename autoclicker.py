import pyautogui
import time
 
def click(): 
    time.sleep(0.0)     
    pyautogui.click()
 
def main():
    for i in range(20): 
        click()
 
main()