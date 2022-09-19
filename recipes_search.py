from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
    
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.get("https://www.google.com/search?q=receta+con+pollo+,+champiñones+y+zanahoria")

recipecount = len(driver.find_elements(By.XPATH, "//*[@id='rso']/div"))

print(recipecount)

for i in range(recipecount):
    try:
        url = driver.find_element(By.XPATH, "//*[@id='rso']/div["+str(i+1)+"]/div/div[1]/div[1]/div/a")
        print(url.get_attribute('href'))
    except NoSuchElementException:
        continue

driver.close()