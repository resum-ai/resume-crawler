import json
import jobkorea
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import ssl
import os

with open("secrets.json", "r") as secret_file:
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
file = open("/Users/jang-youngjoon/학교/2023-2학기/졸프/jobkorea_link.txt", "r")

driver.get(jobkorea_login_url)

read_count = 1

qa_data = []

while True:
    file_url = file.readline()
    print(read_count, "번째 줄")

    if file_url == "":
        break

    try:
        question_list, answer_list = jobkorea.self_introduction_crawl(driver=driver, file_url=file_url)

        for index in range(len(question_list)):
            qa_data.append({
                "Question": f"{question_list[index]}",
                "Answer": f"{answer_list[index]}"
            })

        print(qa_data)
        print(len(qa_data))

    except Exception as e:
        print(f"{read_count}번째에서 다음 에러가 발생했습니다: {e}")

    read_count += 1
