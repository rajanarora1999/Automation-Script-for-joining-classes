from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import calendar
import time
from datetime import date
def login():
	global driver
	# url of gmail
	url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
	print("Opening gmail login ")
	driver.get(url)
	username=driver.find_element_by_id("identifierId")
	print('enter username=')
	use=input()
	username.send_keys(use)
	driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
	time.sleep(7)
	passwordk=driver.find_element_by_name("password")
	print('enter password :')
	passwo=input()
	passwordk.send_keys(passwo)
	driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
	time.sleep(2)
def join_classes(classes) :
	global driver
	for i in range(len(classes)):
		print("Opening class number {}".format(i+1))
		driver.get(classes[i])
		time.sleep(3)
		try:
			driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div").click()
		except:
			pass
		if i==0 :
			print("Allow/Block camera and mic permissions manually")
		time.sleep(3)
		driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]").click()
		time.sleep(3)
		try:
			driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[2]/div[3]/div").click()
			time.sleep(2)
		except :
			pass
		driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[3]/div/div").click()
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[1]/div/div/div").click()
		if i==0 :
			time.sleep(3840)
		else :
			time.sleep(3720)
		if i==len(classes)-1:
			print(" Classes Over")
			driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div").click()
			return ;
		print("Leaving class number {}".format(i+1))

def main():
	global driver
	days=["Monday", "Tuesday", "Wednesday","Thursday","Friday"]
	url_list={"itac":"https://meet.google.com/lookup/b6ls7ceypo","eco":"https://meet.google.com/lookup/bldr52y2r4",
	"antenna":"https://meet.google.com/lookup/gsilerzv5m","control" :"https://meet.google.com/lookup/gerwnm67wp",
	"vlsi":"https://meet.google.com/lookup/ao7bjh2bad",
	"micro":"https://meet.google.com/eei-jcws-bfg"
	}
	current_date = date.today()
	print("Date is {}".format(current_date))
	day=days[current_date.weekday()]
	print("Day is {}".format(day))
	print("Opening Classes For  {}".format(day))
	login()
	if(day=="Monday") :
		classes=[url_list["itac"],url_list["eco"],url_list["antenna"],url_list["control"]]
		join_classes(classes)
	if(day=="Tuesday") :
		classes=[url_list["vlsi"],url_list["itac"],url_list["eco"],url_list["antenna"]]
		join_classes(classes)
	if(day=="Wednesday") :
		classes=[url_list["micro"],url_list["vlsi"],url_list["itac"],url_list["eco"]]
		join_classes(classes)
	if(day=="Thursday") :
		classes=[url_list["control"],url_list["micro"],url_list["vlsi"]]
		join_classes(classes)
	if(day=="Friday") :
		classes=[url_list["antenna"],url_list["control"],url_list["micro"]]
		join_classes(classes)


if __name__ == '__main__':
	driver = webdriver.Chrome('chromedriver.exe')
	main()