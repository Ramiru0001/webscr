import chromedriver_binary # nopa
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import sys
sys.path.append("C:\\Program Files\\Google\\Chrome\\Application")
exception_type, exception_object, exception_traceback = sys.exc_info()
import traceback

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
#options.add_argument('--headless')
driver_path = "./chromedriver"
print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

url = 'https://kakaku.com/'

try:
    driver.get(url)

    search_bar = driver.find_element(By.NAME,'query')
    search_bar.send_keys("nintendo switch")
    driver.find_element(By.NAME,'search').click() 
    dropdown=driver.find_elements(By.CLASS_NAME, 'p-pullDown_list')[0]
    print(F"dropdown={dropdown}")
    
    dropdown.click()


#driver.find_elements(By.NAME,'search').click() #btnKが2つあるので、その内の後の方
#print(driver.current_url)
except Exception as e:
                print(f"エラー: {e}")
                traceback.print_exc()
    

#検索結果の一覧を取得する
# results = []
# flag = False
# while True:
#     g_ary = driver.find_elements_by_class_name('g')
#     for g in g_ary:
#         result = {}
#         result['url'] = g.find_element_by_class_name('yuRUbf').find_element_by_tag_name('a').get_attribute('href')
#         result['title'] = g.find_element_by_tag_name('h3').text
#         results.append(result)
#         if len(results) >= 50: #抽出する件数を指定
#             flag = True
#             break
#     if flag:
#         break
#     driver.find_element_by_id('pnnext').click()
#     time.sleep(INTERVAL)


#10秒間待機
time.sleep(10) 

#chromeを閉じる
#driver.close() 

# ブラウザを終了する
#driver.quit()
