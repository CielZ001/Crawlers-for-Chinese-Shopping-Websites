import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import imageio
from imageio.core.functions import imread
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import pandas as pd



def get_good(price,driver):
    try:
        # num = 0
        time.sleep(5)
        js_code = '''
        window.scrollTo(0,5000)
        '''
        driver.execute_script(js_code)
        try:
            choose_tag = driver.find_element(By.XPATH,'//*[@id="J_filter"]/div[1]/div[1]/a[2]')
            # choose_tag = driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]')
            print(choose_tag)
            choose_tag.click()
        except:
            choose_tag = driver.find_element(By.XPATH,'//*[@id="J_filter"]/div[1]/div[1]/a[2]')
            # choose_tag = driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]')
            print(choose_tag)
            choose_tag.click()
        
        time.sleep(5)
        good_list = driver.find_elements(By.CLASS_NAME,'gl-item')
        # good_list = driver.find_elements_by_class_name('gl-item')
        for good in good_list:
            good_price = good.find_element(By.CSS_SELECTOR,'.p-price i').text
            # good_name = good.find_element_by_css_selector('.p-name em').text
            # print(num)
            price.append(good_price)
            print(good_price)
            # num += 1
            # with open('static/jdBrand.txt', 'a', encoding='utf-8') as f:
            #     f.write(good_name)
        # 找到页面下一页点击
        next_tag = driver.find_element(By.CLASS_NAME,'pn-next')
        # next_tag = driver.find_element_by_class_name('pn-next')
        next_tag.click()

        time.sleep(5)
        
        # count = 0
        # get_good(driver)
        
        # while(num<200):
        #     driver.close()
            # count=count+1     
        
    except:
        # driver.close()
        print("未知异常")

if __name__=='__main__':
    s = Service(r"D:/webdriver/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    # driver = webdriver.Chrome(r'D:/webdriver/chromedriver.exe')
    # jdStr=[]
# num = 1
    try:
        driver.implicitly_wait(10)
        driver.get('https://www.jd.com/')
        gPrice = []

        # input_tag = driver.find_element_by_id('key')
        input_tag = driver.find_element(By.ID,'key')
        input_tag.send_keys('教育机器人')
        input_tag.send_keys(Keys.ENTER)
        count = 0
        while(count<4):
            get_good(gPrice,driver)
            count+=1
            
        df = pd.DataFrame(gPrice)
        # df["price"] = ilt
        df.to_csv("priceJD.csv", mode='a', encoding='utf-8', index=False)
        print('商品信息写入成功！')
        
        # ConvertStr = ''
        # for i, item in enumerate(infoList):
        #     ConvertStr += item[0].strip()

        # with open('static/content.txt', mode='w', encoding='utf-8') as f:
        #     f.write(ConvertStr)
        
    finally:
        driver.close()
    

