from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request
import ssl
import os
import requests

# ssl certification 오류 해결
ssl._create_default_https_context = ssl._create_unverified_context


# selenium option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options.add_argument("--headless"),
)

array = []

for i in range(1, 50):
    driver.get("https://www.jobkorea.co.kr/starter/PassAssay?schPart=10031&schWork=&schEduLevel=&schCType=&schGroup=&isSaved=1&isFilterChecked=1&OrderBy=0&schTxt=&page=" + str(i))
    # page에 따른 경로
    paper_list = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[5]/ul")
    # 자기소개서 목록을 담아놓은 태그
    driver.implicitly_wait(3)
    urls = paper_list.find_elements(By.TAG_NAME, 'a')  # 거기에서 a태그만 가져온다
    for url in urls:
        if 'selfintroduction' in url.get_attribute('href'):
            # 가끔씩 이상한 경로가 섞여들어와서 제외하고 진행했다.
            pass
        else:
            array.append(url.get_attribute('href'))  # href안에 있는 경로를 array에 추가해준다.
array = list(set(array))
print(array)
