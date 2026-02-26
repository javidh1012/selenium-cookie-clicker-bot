from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("http://ozh.github.io/cookieclicker/")



time.sleep(5)
select_language = driver.find_element(By.XPATH,'//*[@id="langSelect-EN"]')
select_language.click()

button = driver.find_element(By.ID,"bigCookie")

end_time = time.time() + 5
game_timing = time.time() + 60 *5

while True:
    button.click()
    cookie = driver.find_element(By.ID, "cookies").text.split()
    cookie_num = int(cookie[0].strip().replace(",",""))
    cursor = driver.find_element(By.XPATH, '//*[@id="product0"]')
    cursor_price = int(driver.find_element(By.ID, "productPrice0").text.strip())
    grand_ma = driver.find_element(By.XPATH, '//*[@id="product1"]')
    grand_ma_price = int(driver.find_element(By.ID, "productPrice1").text.strip())
    if time.time() > end_time:
        if  cookie_num >= grand_ma_price:
            grand_ma.click()
            end_time = time.time() + 5
        elif cookie_num >= cursor_price:
            cursor.click()
            end_time = time.time() + 5
    if time.time() > game_timing:
        print(f"Final result :{cookie_num}")
        driver.quit()
        break

button = driver.find_element(By.ID,"bigCookie")
end_time = time.time() + 5
game_timing = time.time() + 60 *5

while True:
    button.click()
    cookie = driver.find_element(By.ID, "cookies").text.split()
    cookie_num = int(cookie[0].strip().replace(",",""))
    cursor = driver.find_element(By.XPATH, '//*[@id="product0"]')
    cursor_price = int(driver.find_element(By.ID, "productPrice0").text.strip())
    grand_ma = driver.find_element(By.XPATH, '//*[@id="product1"]')
    grand_ma_price = int(driver.find_element(By.ID, "productPrice1").text.strip())
    if time.time() > end_time:
        if  cookie_num >= grand_ma_price:
            grand_ma.click()
            end_time = time.time() + 5
        elif cookie_num >= cursor_price:
            cursor.click()
            end_time = time.time() + 5
    if time.time() > game_timing:
        print(f"Final result :{cookie_num}")
        driver.quit()
        break
