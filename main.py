from selenium import webdriver
from selenium.webdriver.common.by import  By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org")

upcoming_events_names=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
upcoming_events_dates=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
upcoming_events ={}
for n in range(0,len(upcoming_events_names)):
    upcoming_events.update({n:{"Time":upcoming_events_dates[n].text,"name":upcoming_events_names[n].text}})


print(upcoming_events)
