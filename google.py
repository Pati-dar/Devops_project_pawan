from selenium import webdriver

driver- webdriver.Chrome()

driver.get("https://www.google.com")


search_box= driver.find_element("name","q")
search_box.send_keys("OpenAI Chatgpt")

search_box.submit()

driver.implicitly_wit(10)
print("Page titile: ", driver.title )

driver.quit()