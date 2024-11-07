import chromedriver_binary # nopa
from selenium import webdriver

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
#options.add_argument('--headless')

print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.co.jp')

search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
#print(driver.current_url)

# ブラウザを終了する
#driver.quit()
