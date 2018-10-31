from selenium import webdriver
from selenium.webdriver.common.keys import Keys  

test_inputs = ["name", "about", "education", "skills", "work", "contact"]

def test_home():
	driver = webdriver.Chrome()
	driver.get("http://162.246.157.115:8000/")

	for i in test_inputs:
		elem = driver.find_element_by_id(i)
		assert elem != None

