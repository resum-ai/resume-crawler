import json
import jobkorea
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import ssl
import os

with open('secrets.json', 'r') as secret_file:
    secrets = json.load(secret_file)

jobkorea_login_url = secrets["LOGIN_URL"]

# SSL 인증 오류 해결
ssl._create_default_https_context = ssl._create_unverified_context

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options.add_argument("--headless"),
)
file = open('/Users/jang-youngjoon/학교/2023-2학기/졸프/jobkorea_link.txt','r')

driver.get(jobkorea_login_url)

while True:
    file_url = file.readline()
    print(file_url)
    if file_url == "":
        break
    jobkorea.self_introduction_crawl(driver=driver, file_url=file_url)



