from selenium import webdriver
from getpass import getpass
import time
username = input("Enter your username(Should be greater than 6 letters: ")
password = getpass('Enter your password')
chrome = webdriver.Chrome('/root/Downloads/chromedriver')
chrome.get('http://www.babblenow.com')

uname = chrome.find_element_by_id('login-username')
uname.send_keys(username)

passwd = chrome.find_element_by_id('login-password')
passwd.send_keys(password)

submit = chrome.find_element_by_xpath("//button[@class='btn btn-primary btn-block']")
submit.click()
for i in range(20):
	c_id = random.randrange(42000000,80000000)
	vote_click = chrome.find_element_by_xpath("//span[@onmousedown='upvote(c_id,this)'][@class data-toggle='tooltip']")
	vote_click.click()
