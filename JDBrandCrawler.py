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



def get_good(driver):
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
            good_name = good.find_element(By.CSS_SELECTOR,'.p-shop a').text
            # good_name = good.find_element_by_css_selector('.p-name em').text
            # print(num)
            print(good_name)
            # num += 1
            with open('static/jdBrand.txt', 'a', encoding='utf-8') as f:
                f.write(good_name)
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

def jieba_processig(stop_word, text):
    '''jieba分词'''
    with open(stop_word, 'r', encoding='utf-8', errors='ignore') as f:
        stop_words = f.read().splitlines()

    with open(text, 'r', encoding='utf-8') as fi:

        jieba.add_word('细思极恐')
        # jieba.add_word('快银')
        cut_str = '/'.join(jieba.cut(fi.read(), cut_all=False))

    cut_word = []
    for word in cut_str.split('/'):
        if word not in stop_words and len(word) > 1:
            cut_word.append(word)

    return ' '.join(cut_word)


if __name__=='__main__':
    s = Service(r"D:/webdriver/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    # driver = webdriver.Chrome(r'D:/webdriver/chromedriver.exe')
    # jdStr=[]
# num = 1
    try:
        driver.implicitly_wait(10)
        driver.get('https://www.jd.com/')

        # input_tag = driver.find_element_by_id('key')
        input_tag = driver.find_element(By.ID,'key')
        input_tag.send_keys('教育机器人')
        input_tag.send_keys(Keys.ENTER)
        count = 0
        while(count<4):
            get_good(driver)
            count+=1
        print('商品信息写入成功！')
        
        # ConvertStr = ''
        # for i, item in enumerate(infoList):
        #     ConvertStr += item[0].strip()

        # with open('static/content.txt', mode='w', encoding='utf-8') as f:
        #     f.write(ConvertStr)

        back_coloring = imread('static/robot.png')

        wc = WordCloud(background_color='white',
                    scale=5,
                    max_words=600,
                    mask=back_coloring,
                    stopwords='static/baidu_stopwords.txt',
                    font_path='static/font.ttf',  # 设置中文字体
                    max_font_size=60,  # 设置字体最大值
                    random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                    width=600,
                    height=600).generate(jieba_processig('static/baidu_stopwords.txt', 'static/jdBrand.txt'))
        pUrl = "static/wordcloudJDBrand.png"
        wc.to_file(pUrl)
        
    finally:
        driver.close()
    

