import json
import jobkorea
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import ssl
import os
import sqlite3

with open("secrets.json", "r") as secret_file:
    secrets = json.load(secret_file)

jobkorea_login_url = secrets["LOGIN_URL"]

# 데이터베이스 연결
conn = sqlite3.connect('crawling_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS data
                  (Question TEXT, Answer TEXT)''')

# 데이터 저장 함수
def save_to_db(question, answer):
    # 중복 검사
    cursor.execute("SELECT * FROM data WHERE Question = ? AND Answer = ?", (question, answer))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO data (Question, Answer) VALUES (?, ?)", (question, answer))
        conn.commit()

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

# 처음 n줄을 건너뛰기
crawled = 499
for _ in range(crawled):
    next(file)

driver.get(jobkorea_login_url)

read_count = crawled

qa_data = []

while True:
    file_url = file.readline()
    print(read_count, "번째 줄")

    if file_url == "":
        break

    try:
        qa_result = jobkorea.self_introduction_crawl(driver=driver, file_url=file_url)
        question_list = qa_result["question_list"]
        answer_list = qa_result["answer_list"]

        for index in range(len(question_list)):
            question = question_list[index]
            answer = answer_list[index]

            # DB에 저장
            save_to_db(question, answer)

            qa_data.append({
                "Question": question,
                "Answer": answer
            })

        print(len(qa_data))

    except Exception as e:
        print(f"{read_count}번째에서 다음 에러가 발생했습니다: {e}")

    read_count += 1