import sys
sys.path.append("C:\\Program Files\\Google\\Chrome\\Application")
sys.path.append("C:\\Users\\shian\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages")
exception_type, exception_object, exception_traceback = sys.exc_info()
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
import traceback
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import StaleElementReferenceException
# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--mute-audio')
options.add_argument('--disable-webaudio')
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driber_path=".//chromedriver-win64"
# ドライバの相対パスを設定
driver_path = os.path.join('..', 'chromedriver-win64', 'chromedriver.exe')
service = Service(driver_path)

chrome_path= os.path.join('..', 'chrome-win64', 'chrome.exe')
options.binary_location = chrome_path

driver = webdriver.Chrome(service=service,options=options)
url = 'http://gapoli.net/'

try:
    driver.get(url)
    time.sleep(3) 

    try:
        # 全てのコンテンツが読み込まれるまで待機
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)

    except TimeoutException as e:
        print(f"timeout: {e}")
        traceback.print_exc()
            
    login_btn = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/button[1]')
    login_btn.click()
    time.sleep(2) 
    mail_address_input=driver.find_element(By.ID,'loginID')
    password_input=driver.find_element(By.ID,'loginPassword')
    
    mail_address_input.send_keys("shian2528@gmail.com")
    password_input.send_keys("Lar22015")
    time.sleep(1) 
    btn=driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/div/form/div[2]/div/button')
    btn.click()
    
    try:
        # 全てのコンテンツが読み込まれるまで待機
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)

    except TimeoutException as e:
        print(f"timeout: {e}")
        traceback.print_exc()
    
    
    def popup_delete():
        print("ポップアップを消去します")
        try:
        #現在あるポップアップを入手する
            all_pop=driver.find_elements(By.CLASS_NAME,'_overLayer_pyhvt_7')
            #popupの種類を入手する
            for i in range(len(all_pop)):
            
                elements1=all_pop[i].find_elements(By.CLASS_NAME,'_buttonGroup_15bgs_30')
                elements2=all_pop[i].find_elements(By.CLASS_NAME,'_buttonGroup_1wd4r_273')
                elements3=all_pop[i].find_elements(By.CLASS_NAME,'_closeContainer_18ajx_30')
            
            if len(elements1)!=0:
                #アプリのop
                path='./button[2]'
                elements1[0].find_element(By.XPATH,path).click()
                
            if len(elements2)!=0:
                #動画のop
                path='./button[1]'
                elements2[0].find_element(By.XPATH,path).click()
            if len(elements3)!=0:
                #ゲーム復帰のpop
                elements3[0].click()
            
            time.sleep(1) 
        except StaleElementReferenceException as e:
            print(f"エラー：{e}")
            return
        return
    
    time.sleep(5) 
    popup_delete()
    time.sleep(1) 
    popup_delete()
    time.sleep(1)
    popup_delete()
    time.sleep(3) 
    
    # taphere=driver.find_element(By.CLASS_NAME,'_scroller_cqpf6_15')
    # taphere.find_element(By.CLASS_NAME,'_iframe_cqpf6_8').click()
    print("タップで開始ボタンを押します")
    driver.find_element(By.CLASS_NAME,'_autoToggle_1s4tx_31').click()
    
    print("autoボタンを押します")
    time.sleep(1) 
    
    changebtn=driver.find_elements(By.CLASS_NAME,'_selectButton_1wd4r_200')
    
    time.sleep(1) 
    if(len(changebtn)!=0):
        changebtn[0].click() 
        
    time.sleep(30) 
    print("autoボタンを押します")
    driver.find_element(By.CLASS_NAME,'_autoToggle_1s4tx_31').click()
    
except Exception as e:
    print(f"エラー: {e}")
    traceback.print_exc()

os.system("pause")

    #それによって種類を変える
    #3種類とも終わったら次の処理
    
    #popupの種類を入手する
    
    
    # #現在あるポップアップを入手する
    # all_pop=driver.find_elements(By.CLASS_NAME,'_overLayer_pyhvt_7')
    # #popupの種類を入手する
    # for i in range(len(all_pop)):
    #     if all_pop[i].find_element(By.CLASS_NAME,'_paragraphXS_e96vf_103')!=None:
    #         #アプリのop
    #         path='../div[3]/div[2]'
    #         driver.find_element(By.XPATH,path).click()
    #     elif all_pop[i].find_element(By.CLASS_NAME,'_paragraphS_e96vf_92')!=None:
    #         #動画のop
    #         path='div[4]/button[1]'
    #         driver.find_element(By.XPATH,path).click()
    #     elif all_pop[i].find_element(By.CLASS_NAME,'_paragraphM_e96vf_81')!=None:
    #         #ゲーム復帰のpop
    #         path='../div[3]/button[2]'
    #         driver.find_element(By.XPATH,path).click()
        
    #     time.sleep(1) 
    
    # wait = WebDriverWait(driver,10)
    
    # try:
    #     wait.until(EC.alert_is_present())   #Javascriptのアラートがでてくるまで待つ
    #     Alert(driver).accept()         #アラート受け入れる(OKを押す)        
    #     time.sleep(1) #1秒まつ
    
    # except Exception as e:
    #     print("アラートの処理でエラー")
    
   
    
    # time.sleep(1) 
    # path='//*[@id="root"]/div/div[6]/div[2]/div/div/div[2]/div[3]/button[2]'
    # if  driver.find_element(By.XPATH,path) != None:
    #     driver.find_element(By.XPATH,path).click()
    # time.sleep(1) 
    # path='//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div/div[4]/button[1]'
    # if  driver.find_element(By.XPATH,path) !=None:
    #     driver.find_element(By.XPATH,path).click()
    # time.sleep(1) 
    # path='//*[@id="root"]/div/div[3]/div[3]/div/div/div[2]/div[3]/label/input'
    # if  driver.find_element(By.XPATH,path)!=None:
    #     driver.find_element(By.XPATH,path).click()
    #     driver.find_element(By.CSS_SELECTOR,'_closeContainer_18ajx_30').click()
        
#driver.find_elements(By.NAME,'search').click() #btnKが2つあるので、その内の後の方
#print(driver.current_url)

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


#chromeを閉じる
#driver.close() 

# ブラウザを終了する
#driver.quit()
