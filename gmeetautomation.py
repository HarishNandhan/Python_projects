from time import sleep
import pyautogui as auto
import schedule, webbrowser
webbrowser.register('chrome',None)
 
link="meet.google.com/lookup/a2wzlppz2y"

time= "09:01"

def join():
	webbrowser.open_new_tab('https://'+ link)
	sleep(7)
	auto.hotkey('ctrl',	'd')
	auto.hotkey('ctrl',	'e')
	auto.click(1331, 612)

schedule.every().day.at(time).do(join)

while True:
	schedule.run_pending()
	sleep(1)

