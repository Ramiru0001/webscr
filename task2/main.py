import requests
import chromedriver_binary # nopa
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd
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

url = 'http://qiita.com/advent-calendar/2016/crawler'

try:
    driver.get(url)
    # 全てのコンテンツが読み込まれるまで待機
    try:
        # 全てのコンテンツが読み込まれるまで待機
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)

    except TimeoutException as e:
        print(f"timeout: {e}")
        traceback.print_exc()
    
    all_url=[]
    all_text=[]
    allday=driver.find_elements(By.CLASS_NAME,"style-1dw8kp9")
    for i in range(len(allday)):
        oneday=allday[i].find_element(By.CLASS_NAME,"style-14mbwqe")
        if oneday.text=="":
            break
        all_text.append(oneday.text)
        all_url.append(oneday.get_attribute("href"))
        print(F"{[i]} url:{all_url[i]} text:{all_text[i]}")
    
    #隠されてたリストを表示
    # tag = driver.find_element(By.CSS_SELECTOR,".p-pullDown_list")

    # driver.execute_script("arguments[0].setAttribute('style','display: block;')", tag)
    

    #リストから選択
    # dropdown=driver.find_elements(By.CLASS_NAME, 'p-pullDown_list')

    # dropdown1=driver.find_element(By.XPATH, '//*[@id="default"]/div[2]/div[2]/div/div[3]/div[2]/div/div/ul/li[1]')

    # count = len(dropdown)
    # print(f"リストの様子数＝{count}")

    
    # dropdown1.click()

    try:
        # 全てのコンテンツが読み込まれるまで待機
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)
        
    except TimeoutException as e:
        print(f"timeout: {e}")
        traceback.print_exc()
    
    #elems = driver.find_elements('th')

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
