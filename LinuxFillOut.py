from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import os
import sys

"""
- 利用 crontab 來做 Linux 固定排程:

    https://code.kpman.cc/2015/02/11/%E5%88%A9%E7%94%A8-crontab-%E4%BE%86%E5%81%9A-Linux-%E5%9B%BA%E5%AE%9A%E6%8E%92%E7%A8%8B/

    crontab權限(這裡很亂，還跟python環境有關):
        1. https://blog.gtwang.org/linux/linux-crontab-cron-job-tutorial-and-examples/
        2. https://ithelp.ithome.com.tw/questions/10186256
        
    如果是裝pyenv來管理python環境的話，要注意crontab當下的python環境是哪個

- 要起在linux，必須先裝chrome，然後在資料夾內放相對應版本的chromedriver

參考: https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome/24364290#24364290

1. Check you have installed latest version of chrome brwoser-> chromium-browser -version
2. If not, install latest version of chrome sudo apt-get install chromium-browser
3. get appropriate version of chrome driver from here
4. Unzip the chromedriver.zip
5. Move the file to /usr/bin directory sudo mv chromedriver /usr/bin
6. Goto /usr/bin directory cd /usr/bin
7. Now, you would need to run something like sudo chmod a+x chromedriver to mark it executable.
8. finally you can execute the code.

    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    print driver.page_source.encode('utf-8')
    driver.quit()
    display.stop()

裝chrome on linux (binary):

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
    sudo yum install google-chrome-stable_current_x86_64.rpm

裝相對應版本chromedriver:

    https://chromedriver.chromium.org/downloads

Trouble Shooting:

    https://blog.csdn.net/ouyanggengcheng/article/details/90476553
"""


sys.path.append("./chromedriver_linux64")
#今天講個特別的，我們可以不讓瀏覽器執行在前景，而是在背景執行（不讓我們肉眼看得見）
#如以下宣告 options
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.binary_location = "/usr/bin/google-chrome"
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument('--disable-dev-shm-usage')

#打開瀏覽器,確保你已經有chromedriver在你的目錄下
# 然後將options加入Chrome方法裡面，至於driver請用executable_path宣告進入
browser = webdriver.Chrome(executable_path='/自動填表單程式/chromedriver_linux64/chromedriver', chrome_options=option)

# #在瀏覽器打上網址連入
url = "The URL You Wanna Go To"
browser.get(url)

# 這時候就可以分析網頁裡面的元素
# find_element_by_XXX: https://selenium-python.readthedocs.io/locating-elements.html
element_1 = browser.find_element_by_id('486014833_3209788694')

# https://blog.csdn.net/WanYu_Lss/article/details/84137519
# 直接下element.click的話找到兩個元素會出錯
browser.execute_script("arguments[0].click();", element_1)

time.sleep(1)

# 對空格填入
element_2 = browser.find_element_by_id('486014830')
element_2.send_keys("123456")

time.sleep(1)

# radio-button (不同選項id會不同)
element_3 = browser.find_element_by_id('486014835_3209788699')
browser.execute_script("arguments[0].click();", element_3)

time.sleep(1)

my_temp = random.randrange(364, 370) / 10
element_4 = browser.find_element_by_id('486014831')
element_4.send_keys(str(my_temp))

time.sleep(1)

# 選否
element_5 = browser.find_element_by_id('486015076_3209796414')
browser.execute_script("arguments[0].click();", element_5)

time.sleep(1)

# 已詳閱規定
element_6 = browser.find_element_by_id('486014832_3209788684')
browser.execute_script("arguments[0].click();", element_6)

# 下一頁 (xpath可以F12，選取後右鍵直接copy，很方便)
element_7 = browser.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button')
element_7.click()

time.sleep(3)

# 最後關閉視窗 (這邊要等瀏覽器跑一下)
element_8 = browser.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button')
element_8.click()

# 關閉瀏覽器
browser.close()